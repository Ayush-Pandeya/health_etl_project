# Health ETL Pipeline

A complete local ETL pipeline built with Airflow, PySpark, Streamlit, OpenLineage, and AWS S3.

## Features
- Extract-transform-load data
- Airflow orchestration
- Lineage tracking via OpenLineage
- Streamlit dashboard
- Flask receiver for lineage events
- Parquet export to local/S3

## Setup

```bash
pip install -r requirements.txt
python main.py         # Run ETL
streamlit run streamlit_app/dashboard.py
python streamlit_app/lineage_catcher.py  # Flask lineage listener
```