@echo off
:: اضبط المسارات التالية
set DASHBOARD_PATH="C:\desktop folders__\projects\Project_1\Chemical-Data-Pipeline\dashboard.py"
set PYTHON_EXE="C:\Users\scisa\miniconda3\envs\chem_new\Scripts\streamlit.exe"

:: تشغيل الداشبورد وفتح المتصفح تلقائياً
%PYTHON_EXE% run %DASHBOARD_PATH%

pause