from include.pokemon_api import RequestPokemon
from include.enviar_bucket import EnviarParaBucket
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "Astro", "retries": 3},
    tags=["pokemon"],
)
def dag_pokemon():

    @task
    def capturar_pokemon():
        return RequestPokemon().dados_pokemon()

    capturar_pokemon()

    @task
    def enviar_bucket():
        return EnviarParaBucket().executar_backup()

    executar_request = capturar_pokemon()
    salvar_bucket = enviar_bucket

    executar_request >> salvar_bucket

dag_pokemon()
