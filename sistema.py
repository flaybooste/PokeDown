import os
from db import Database

def changename(id):
    for x in os.listdir("img"):
        pos = x.find(".")
        ex = x[pos:]
        os.rename("img/"+x, f"img/{str(Database().selectdb(id)[0])+ex}")
