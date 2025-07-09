from airflow.decorators import dag, task
from datetime import datetime
from time import sleep

@dag(
    dag_id = "primeira_dag",
    start_date = datetime(2025, 7, 8),
    schedule = "@hourly",
    catchup = False
    )

def pipeline():
    @task
    def primeira_funcao():
        print("Executando a primeira função.")
        sleep(3)
    @task
    def segunda_funcao():
        print("Executando a segunda função.")
        sleep(3)
    @task
    def terceira_funcao():
        print("Executando a terceira função.")
        sleep(3)

    extract = primeira_funcao()
    transform = segunda_funcao()
    load = terceira_funcao()

    extract >> transform >> load

pipeline()