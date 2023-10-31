from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BashOperator
from datetime import datetime


def helloWorld():
    print('Hello World')


with DAG(dag_id="hello_world_dag",
         start_date=datetime(2023, 10, 31),
         schedule_interval="@hourly",
         catchup=False) as dag:

    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)

with DAG(dag_id="bash_dag",
         start_date=datetime(2023, 10, 31),
         schedule_interval="@hourly",
         catchup=False) as dag:

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: \'{{ dag_run.conf["message"] if dag_run else "" }}\'"',
    )
