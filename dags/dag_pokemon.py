from include.pokemon_api import RequestPokemon
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
    capturar_pokemon = RequestPokemon().main()
    capturar_pokemon

dag_pokemon()