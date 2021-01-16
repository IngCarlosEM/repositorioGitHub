#__all__ = ["create"]

#Mongo library
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['conexion']
collection = db["Usuarios"]

#Crear funciones de crear, actualizar y borrar (CRUD)

def create(documento):
    collection.insert_one(documento)

def read():
    lista = collection.find()
    return lista

def update(documento):
    myquery = { "nombre": {"$regex": "Carlos"}}
    newvalues = {"$set": {"nombre": "Carlitros"}}
    collection.update_many(myquery, newvalues)

def delete(documento):
    myquery2 = {"nombre": {"$regex": "Carlitros"}}
    collection.delete_many(myquery2)