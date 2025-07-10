import requests
import pandas as pd
from time import sleep
import os


class RequestPokemon():
    def total_pokemon(self):
        # Código para identificar o total de pokemóns listados na API
        # Informação é armazenada em ["count"]
        try:
            url = "https://pokeapi.co/api/v2/pokemon"
            data = requests.get(url).json()
            return int(data["count"])
        except Exception as e:
            raise Exception(f"Não foi possível acessar o link: {e}")


    def dados_pokemon(self):
        pokemons_df = []
        for i in range(0, 41, 20):
        #for i in range(0, self.total_pokemon(), 20):
            print(f"Buscando dados de pokemóns entre {i} e {i+20}")
            page_url = requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={i}&limit=20").json()
            sleep(0.2)
            pokemon_url_list = [result["url"] for result in page_url["results"]]

            for pokemon_url in pokemon_url_list:
                pokemon_data = requests.get(pokemon_url).json()
                pokemon_data = {
                    "id": pokemon_data["id"],
                    "nome": pokemon_data["name"],
                    "altura": pokemon_data["height"],
                    "peso": pokemon_data["weight"],
                    "tipo": [types["type"]["name"] for types in pokemon_data["types"]]
                }
                pokemons_df.append(pokemon_data)
            
            sleep(0.2)
        data_dir = "/tmp/data"
        os.makedirs(data_dir, exist_ok=True)
        pd.DataFrame(pokemons_df).set_index("id").to_json(f"{data_dir}/pokemon_json.json")