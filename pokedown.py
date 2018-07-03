from requests import get
from db import Database

class PokeDown:
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return  "PokeDown class for Poke Project"
    def poke(self):
        req  = get(f"https://pokeapi.co/api/v2/pokemon/{self.id}/")
        pokeid = int(req.json()['id'])
        nomep = req.json()['name'].capitalize()
        nomeh1 = req.json()["abilities"][0]["ability"]["name"].capitalize()
        nomeh2 = req.json()["abilities"][1]["ability"]["name"].capitalize()
        nomeTyp = req.json()["types"][0]["type"]["name"].capitalize()
        Database().inserirdb(pokeid, nomep, nomeh1, nomeh2, nomeTyp)
        return {"id": pokeid ,"nome": nomep, "ability1": nomeh1, "ability2": nomeh2, "type": nomeTyp}
