from pymongo import MongoClient
from Usuarios import users
import sys
#Usuarios de la BD

usuarios = [
    users('Carlos','Esparza','Medel','carlos@ipn.mx'),
    users('Andy','Perez','Martinez','andy@ipn.mx')
] 

#Conexión con BD
client = MongoClient('mongodb://localhost:27017/')

#Crear BD
db = client['conexion']

#Crear una nueva colección
collection = db["Usuarios"]

#Insertar elementos en la colección (tabla)(CREATE)


def create():
    for user in usuarios:
        collection.insert_one(user.toDBCollection())
    return 

create()

def read():
    cursor = collection.find()
    for usr in cursor:
        print(usr)

def update():
    myquery = { "nombre": {"$regex": "Carlos"}}
    newvalues = {"$set": {"nombre": "Carlitros"}}
    collection.update_many(myquery, newvalues)

    collection.update_one(myquery, newvalues)

    return read()

def delete():
    myquery2 = {"nombre": {"$regex": "Carlitros"}}
    collection.delete_many(myquery2)
    return read()
    
read()
update()
delete()