from airflow.sdk.definitions.asset import Asset
from airflow.decorators import dag, task
from pendulum import datetime
import requests
from datetime import datetime

# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Diogo", "retries": 3},
    tags=["hello_world_dag"],
)


def hello_world():
    print("Hello World Airflow!")

hello_world()