from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago
from pathlib import Path

import sys

default_args = {
    "owner": "Airflow",
    "start_date": days_ago(2),

}

PATHS = sys.path

username = "span"
home_dir = Path("/home", username)
outputs_dir = Path(home_dir, "outputs")
module_path = Path('/opt/airflow/dags/span/my_modules')

PATHS.append(str(module_path))

from pyodbc_conn import odbc_exec

def print_callable():
    import sys as s
    print("dag level paths:")
    print(PATHS)
    print("task level paths:")
    print(s.path)

with DAG(
    dag_id="example_dag",
    default_args=default_args,
    start_date=datetime(2022, 1, 1),
    schedule_interval="* * * * *",
    catchup=False) as dag:

    task1 = PythonOperator(
        task_id="print_task",
        python_callable=print_callable)
