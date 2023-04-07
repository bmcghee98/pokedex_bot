import requests

#pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
#type_url = "https://pokeapi.co/api/v2/type/"

def get_pokemon(poke_name):
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/" 
    pokemon_url += poke_name

    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()  
        return data
    else:
        print("Error:", response.status_code)

def get_type(type_name):
    type_url = "https://pokeapi.co/api/v2/type/"
    type_url += type_name

    response = requests.get(type_url)

    if response.status_code == 200:
        data = response.json()  
        return data
    else:
        print("Error:", response.status_code)

def get_desc(poke_name):
    species_url = "https://pokeapi.co/api/v2/pokemon-species/"
    species_url += poke_name

    response = requests.get(species_url)

    if response.status_code == 200:
        data = response.json()  
        return data
    else:
        print("Error:", response.status_code)
