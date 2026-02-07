import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Chemical Research Dashboard", layout="wide")

st.title("🧪 Chemical Compounds Analysis Dashboard")
st.write("Interactive visualization of chemical data from SQLite database")

# 2. Data Loading & Cleaning
def load_data():
    conn = sqlite3.connect('Chemical_Research.db')
    df = pd.read_sql('SELECT * FROM Compounds_Table', conn)
    conn.close()
    
    # Ensuring numeric types to avoid TypeErrors
    df['MW'] = pd.to_numeric(df['MW'], errors='coerce')
    df['LogP'] = pd.to_numeric(df['LogP'], errors='coerce')
    return df.dropna(subset=['MW', 'LogP'])

try:
    df = load_data()

    # 3. Sidebar Filters
    st.sidebar.header("🔍 Search Filters")
    all_compounds = df['Name'].unique()
    selected_mol = st.sidebar.multiselect("Select Compounds:", all_compounds, default=all_compounds)

    filtered_df = df[df['Name'].isin(selected_mol)]

    # 4. Key Metrics
    col1, col2, col3 = st.columns(3)
    if not filtered_df.empty:
        col1.metric("Total Compounds", len(filtered_df))
        col2.metric("Average MW", f"{round(filtered_df['MW'].mean(), 2)} g/mol")
        col3.metric("Max LogP", round(filtered_df['LogP'].max(), 2))

    # 5. Interactive Charts (Plotly)
    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Molecular Weight Comparison")
        fig1 = px.bar(filtered_df, x='Name', y='MW', color='LogP', 
                     color_continuous_scale='Viridis', template='plotly_white',
                     labels={'MW': 'Molecular Weight', 'Name': 'Compound Name'})
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.subheader("MW vs LogP Relationship")
        fig2 = px.scatter(filtered_df, x='MW', y='LogP', text='Name', size='MW', 
                         color='Name', template='plotly_white',
                         labels={'MW': 'Molecular Weight', 'LogP': 'LogP Value'})
        st.plotly_chart(fig2, use_container_width=True)

    # 6. Detailed Data Table
    st.subheader("📋 Raw Data Table")
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"Error loading dashboard: {e}")