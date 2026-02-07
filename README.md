 # 🧪 Automated Chemoinformatics Pipeline & Interactive Dashboard

## 📖 Project Overview
This project represents a complete **End-to-End Data Engineering** solution tailored for **Organic Chemistry** research. The pipeline automates the extraction of chemical data, performs molecular property calculations, stores them in relational databases, and provides a real-time interactive UI for researchers to screen compounds.

---

## 🛠 Project Architecture & Workflow

### 1. Data Acquisition & Processing 🔄
* **API Integration**: Automated fetching of molecular data (SMILES, Names) from the **PubChem API**.
* **Property Calculation**: Used **RDKit** to compute essential molecular descriptors like **Molecular Weight (MW)** and **LogP**.
* **Data Cleaning**: Handled data types using **Pandas**, ensuring all molecular properties are converted to numeric formats to prevent calculation errors.

### 2. Database Management (The Storage Layer) 💾
* **SQLite (Local Storage)**: Used as a lightweight initial storage for research data (`Chemical_Research.db`).
* **SQL Server (Enterprise Layer)**: Migrated the final cleaned dataset (`Compounds_Master`) to **Microsoft SQL Server (SSMS)** using `SQLAlchemy` and `pyodbc` for enterprise-level persistence and security.
* **Dynamic SQL Querying**: Implemented complex SQL queries to filter high-molecular-weight compounds (e.g., $MW > 200$) directly from the database.
 ### 🗄️ SQL Server Persistence
 
<img width="1892" height="1041" alt="sql_database_view png" src="https://github.com/user-attachments/assets/8937cdc9-7051-4021-8c02-b16f43a01525" />


### 3. Interactive Visualization (The Dashboard) 📊
* **Framework**: Built with **Streamlit** to create a responsive web application.
* **Visuals**: Leveraged **Plotly Express** for dynamic scatter plots (MW vs LogP) and bar charts.
* **Interactive UI**: Users can search for specific compounds and filter the entire dashboard view in real-time via sidebar controls.
 ### 📊 Dashboard Overview
 <img width="1920" height="1039" alt="dashboard_preview png" src="https://github.com/user-attachments/assets/c08ef90b-feab-423b-be28-8fe770956d53" />
 
---


## 🚀 Key Features
* **Full ETL Pipeline**: Extract, Transform, and Load (ETL) from API to SQL Server.
* **Error Handling**: Robust error management for data type conversion and database connectivity.
* **Metric Tracking**: Automated calculation of average MW and maximum LogP for selected compound batches.

---

## 🛠 Tech Stack
| Category | Tools & Libraries |
| :--- | :--- |
| **Programming** | Python (Pandas, SQLAlchemy, RDKit, PyODBC) |
| **Visualization** | Streamlit, Plotly Express |
| **Databases** | SQLite, Microsoft SQL Server Management Studio (SSMS) |
| **Environment** | Conda / Jupyter Notebook / VS Code |

---

## 📂 Project Structure
* `data_collection.ipynb`: Initial research notebook containing API calls and SQL experiments.
* `dashboard.py`: Core application code for the Streamlit dashboard.
* `Chemical_Research.db`: Local SQLite database containing 10 primary chemical compounds.
* `requirements.txt`: Environment dependencies.

---

## ⚙️ How to Setup & Run
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YourUsername/Chemical-Data-Pipeline.git](https://github.com/YourUsername/Chemical-Data-Pipeline.git)
