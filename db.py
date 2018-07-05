import sqlite3
class Database:
    def __name__(self):
        return "Sqlite3 DATABASE Poke"
    def __init__(self):
        self.con = sqlite3.connect("model/base.db")
        self.cur = self.con.cursor()
    def __repr__(self):
        return f"Sqlite3 db {__name__}"
    def crepoke(self):
        self.cur.execute("CREATE TABLE poke(id INT, pokename TEXT, hab1 TEXT, hab2 TEXT, type TEXT)")
        self.con.commit()
        return f"Database:  {__name__}"
    def inserirdb(self, id, poke, hab1, hab2, tipo):
        self.cur.execute(f"INSERT INTO poke VALUES ({id},'{poke}','{hab1}', '{hab2}','{tipo}')")
        self.con.commit()
        return f"Inserido na tabela poke do banco de dados SQLITE3 --  ID: {id} \t Poke: {poke} \t Habi 1 : {hab1} \t Habi2 {hab2} \t Tipo: {tipo}"
    def selectdb(self, id):
        self.cur.execute(f"SELECT * FROM poke WHERE id = {id}")
        poke = self.cur.fetchone()
        return poke
    def removedb(self, id):
        self.cur.execute(f"DELETE FROM poke WHERE id = {id}")
