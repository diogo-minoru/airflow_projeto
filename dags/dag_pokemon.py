from include.pokemon_api import RequestPokemon
from include.enviar_bucket import EnviarParaBucket
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id = "dag_pokemon",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "Astro", "retries": 3},
    tags=["pokemon"],
)
def dag_pokemon():

    @task
    def capturar_pokemon():
        RequestPokemon().dados_pokemon()

    @task
    def enviar_bucket():
        EnviarParaBucket().executar_backup()

    capturar_pokemon() >> enviar_bucket()

dag_pokemon()
