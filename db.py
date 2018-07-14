import sqlite3
class Pokedb:
    def __name__(self):
        return "Sqlite3 DATABASE Poke"
    def __init__(self):
        self.con = sqlite3.connect("model/base.db")
        self.cur = self.con.cursor()
    def __repr__(self):
        return f"Sqlite3 db {__name__}"
        ##CREATE TABLE
    def create_poke(self):
        self.cur.execute("CREATE TABLE poke(id INT, pokename TEXT, hab1 TEXT, hab2 TEXT, type TEXT)")
        self.con.commit()
        return f"Database:  {__name__}"

        ##Inserir no banco poke
    def inserir_poke_db(self, id, poke, hab1, hab2, tipo):
        self.cur.execute(f"INSERT INTO poke VALUES ({id},'{poke}','{hab1}', '{hab2}','{tipo}')")
        self.con.commit()
        return f"Inserido na tabela poke do banco de dados SQLITE3 --  ID: {id} \t Poke: {poke} \t Habi 1 : {hab1} \t Habi2 {hab2} \t Tipo: {tipo}"
        ##Selecionar item por ID
    def select_one_db(self, id):
        self.cur.execute(f"SELECT * FROM poke WHERE id = {id}")
        poke = self.cur.fetchone()
        return poke
        ##Seleciona todo o banco
    def select_all_db(self):
        self.cur.execute("SELECT * FROM Poke")
        poke = self.cur.fetchall()
        return poke
    def removedb(self, id):
        self.cur.execute(f"DELETE FROM poke WHERE id = {id}")

class PokeUser:
    def __init__(self):
        self.con = sqlite3.connect("model/base.db")
        self.cur = self.con.cursor()
    def create_db_user(self):
        self.cur.execute("CREATE TABLE users(id INT, user TEXT, pass TEXT, pokeid INT)")
        self.con.commit()
        return "Database users criado com sucesso!"
    #Inserir no banco users
    def inserir_users_db(self, id: int, user: str, passw: str, pokeid: int):
        self.cur.execute(f"INSERT INTO users VALUES('{id}', '{user}', '{passw}', '{pokeid}')")
        self.con.commit()
        return f"{id}\t{user}\t{passw}\t{pokeid}"
    #Select user
    def select_user(self, user: str):
        self.cur.execute(f"SELECT * FROM users WHERE user='{user}'")
        user = self.cur.fetchone()
        return user
