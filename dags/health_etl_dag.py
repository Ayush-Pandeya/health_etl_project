from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.save_parquet import save_to_parquet

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
}

with DAG('health_etl_dag', default_args=default_args, schedule_interval=None, catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=lambda: transform_data("data/raw_data.csv")
    )

    validate_task = PythonOperator(
        task_id='validate',
        python_callable=lambda: validate_data("data/transformed_data.csv")
    )

    save_task = PythonOperator(
        task_id='save_parquet',
        python_callable=lambda: save_to_parquet("data/transformed_data.csv")
    )

    extract_task >> transform_task >> validate_task >> save_task
