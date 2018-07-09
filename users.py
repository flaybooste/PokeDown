from db import Database
class Users:
    def __init__(self, ID: int, user: str, passw: str, pokeid: int):
        self.id = id
        self.user = user
        self.passw = passw
        self.pokeid = pokeid
    def __repr__(self):
        return "Classe --> Usuários"
    def insert_users(self):
        Database().inserir_users_db(self.id, self.user, self.passw, self.pokeid)
