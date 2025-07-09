import requests
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon/"

data = requests.get(url).json()

total_pokemons = data["count"]
pokemons = data["results"]
next_page = data["next"]


print(next_page)