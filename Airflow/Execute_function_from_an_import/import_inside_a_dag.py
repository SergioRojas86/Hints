from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.dates import days_ago
from pathlib import Path
from os.path import dirname, realpath
from importlib import import_module
import sys

# this is the configuration in case you need to make an import inside of a dag and execute a function in specific
# here the import comes from a file with classes and functions called pyodbc_conn.py
# the module_path variable contains the location as Airflow distinguish it

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

deployment_dir = dirname(realpath(__file__))
PATHS.append(deployment_dir)

cfg = import_module('pyodbc_conn').TestConfig

#from pyodbc_conn import odbc_exec

with DAG(
    dag_id="example_dag",
    default_args=default_args,
    start_date=datetime(2022, 1, 1),
    schedule_interval="* * * * *",
    catchup=False) as dag:

    task1 = PythonOperator(
        task_id="print_task",
        python_callable=print_callable)

    exec_sproc = PythonOperator(
        task_id='exec_sproc',
        python_callable=cfg.odbc_exec,
        dag=dag
    )
