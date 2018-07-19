from requests import get
from db import Pokedb

class PokeDown:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return  "PokeDown class for Poke Project"
    def pokedb(self):
        req  = get(f"https://pokeapi.co/api/v2/pokemon/{self.id}/")
        pokeid = int(req.json()['id'])
        nomep = req.json()['name'].capitalize()
        nomeh1 = req.json()["abilities"][0]["ability"]["name"].capitalize()
        try:
            nomeh2 = req.json()['abilities'][1]['ability']["name"].capitalize()
        except IndexError:
            nomeh2 = "Não tem segunda habilidade"
            print("não tem habilidade")
        nomeTyp0 = req.json()["types"][0]["type"]["name"].capitalize()
        try:
            nomeTyp1 = req.json()["types"][1]["type"]["name"].capitalize()
        except IndexError:
            Pokedb().inserir1_poke_db(pokeid, nomep, nomeh1, nomeh2, nomeTyp0, '0')
            return {"id": pokeid ,"nome": nomep, "ability1": nomeh1, "ability2": nomeh2, "type0": nomeTyp0}
        Pokedb().inserir1_poke_db(pokeid, nomep, nomeh1, nomeh2, nomeTyp0, nomeTyp1)
        return {"id": pokeid ,"nome": nomep, "ability1": nomeh1, "ability2": nomeh2, "type0": nomeTyp0, "type1": nomeTyp1}
    def pokeselect(self):
        return Pokedb().select_one_db(self.id)
