from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import sqlalchemy as sa
import plotly.express as px
import io

# 1. Page Configuration
st.set_page_config(
    page_title="Molecular Intelligence Pro", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 2. Professional CSS Styling (Global Standard UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp {
        /* Professional Dimmed Chemical Background */
        background: linear-gradient(rgba(10, 15, 25, 0.85), rgba(10, 15, 25, 0.85)), 
                    url('https://images.unsplash.com/photo-1574170623305-6a7f966d974c?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Text High-Visibility Styling */
    h1, h2, h3, h4, h5, p, span, label {
        color: #ffffff !important;
        opacity: 1 !important;
        font-weight: 600 !important;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.5);
    }

    /* Sidebar Glassmorphism Styling */
    [data-testid="stSidebar"] {
        background: rgba(13, 17, 23, 0.95) !important;
        border-right: 2px solid rgba(0, 242, 255, 0.2);
    }

    /* Integrated Dataframe/Table Design */
    [data-testid="stDataFrame"] {
        background: rgba(255, 255, 255, 0.02) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        padding: 5px;
    }

    /* Refresh Button - High-End Gradient */
    .stButton > button {
        background: linear-gradient(135deg, #00f2ff 0%, #7000ff 100%) !important;
        color: white !important;
        font-weight: 800 !important;
        border: none !important;
        border-radius: 12px !important;
        width: 100% !important;
        height: 50px;
        transition: 0.4s all ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 242, 255, 0.4);
    }

    /* Metric Containers Design */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(0, 242, 255, 0.1) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Secure Database Connection Logic
@st.cache_data(ttl=30)
def load_data():
    try:
        connection_url = (
            r"mssql+pyodbc://@SARAMABROUK\DE_FINAL_SQL/Chemistry_DB"
            r"?driver=ODBC+Driver+17+for+SQL+Server"
            r"&trusted_connection=yes"
        )
        engine = sa.create_engine(connection_url)
        df = pd.read_sql("SELECT * FROM Compounds_Master", engine)
        df['MW'] = pd.to_numeric(df['MW'], errors='coerce')
        df['LogP'] = pd.to_numeric(df['LogP'], errors='coerce')
        return df.dropna(subset=['MW', 'LogP']).sort_values(by='MW', ascending=False)
    except Exception as e:
        st.error(f"📡 Database Connection Error: {e}")
        return pd.DataFrame()

# --- Main Application Execution ---
try:
    # Auto-refresh triggers every 60 seconds to pull new SQL data
    st_autorefresh(interval=60000, key="datarefresh")
    
    df = load_data()

    # --- 4. Sidebar Executive Control Panel ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3655/3655580.png", width=80)
        st.markdown("## PROJECT CORE")
        st.markdown("---")
        
        search_name = st.text_input("🔍 Search Molecule", placeholder="Enter name...")
        
        mw_range = st.slider("⚖️ Molecular Weight (MW)", 
                             float(df['MW'].min()), float(df['MW'].max()), 
                             (float(df['MW'].min()), float(df['MW'].max())))
        
        log_val = st.slider("🧪 Lipophilicity (LogP)", 
                               float(df['LogP'].min()), float(df['LogP'].max()), 
                               (float(df['LogP'].min()), float(df['LogP'].max())))
        
        theme = st.selectbox("🎨 Visualization Theme", ["Plasma", "Turbo", "Viridis", "Magma"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button('🔄 REFRESH SYSTEM'):
            st.cache_data.clear()
            st.rerun()

    # --- 5. Real-Time Filtering Logic ---
    filtered_df = df[
        (df['Name'].str.contains(search_name, case=False)) &
        (df['MW'].between(mw_range[0], mw_range[1])) &
        (df['LogP'].between(log_val[0], log_val[1]))
    ]

    # --- 6. Executive Header & Metrics ---
    st.title("🧪 Molecular Intelligence Pro")
    st.markdown("##### Global Chemical Pipeline & Advanced Analytics Dashboard")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Records", f"{len(filtered_df)}")
    m2.metric("Avg Mol. Weight", f"{round(filtered_df['MW'].mean(), 1)}", "u")
    m3.metric("Peak LogP", f"{round(filtered_df['LogP'].max(), 2)}")
    m4.metric("Pipeline Health", "LIVE", delta="Synced")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 7. High-Performance Analytics ---
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 📊 Weight Profile Distribution")
        fig1 = px.bar(filtered_df.head(15), x='Name', y='MW', color='MW',
                     color_continuous_scale=theme, template='plotly_dark')
        fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.markdown("#### 🔬 Molecular Dynamics (LogP vs MW)")
        fig2 = px.scatter(filtered_df, x='MW', y='LogP', color='MW', 
                         size=filtered_df['MW']/10, 
                         hover_name='Name', color_continuous_scale=theme,
                         template='plotly_dark')
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    # --- 8. Master Data Registry & Export Center ---
    st.markdown("---")
    col_title, col_download = st.columns([3, 1])
    
    with col_title:
        st.markdown("#### 📋 Chemical Master Registry")
    
    with col_download:
        # Professional Export Center
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 EXPORT TO CSV",
            data=csv,
            file_name='chemical_master_report.csv',
            mime='text/csv',
        )

    # High-visibility Integrated Dataframe
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ Dashboard System Error: {e}")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("Developed by Sara Mabrouk Engineering | Advanced Cheminformatics Solutions | 2026")
