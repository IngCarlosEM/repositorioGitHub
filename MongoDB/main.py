from pymongo import MongoClient
from Usuarios import users

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
for user in usuarios:
    collection.insert(user.toDBCollection())

#Mostrar todos los elementos de la coleccion (READ)
cursor = collection.find()
for usr in cursor:
    print(usr)

#Actualizar varios elementos de una colección (UPDATE)
myquery = { "nombre": {"$regex": "Carlos"}}
newvalues = {"$set": {"nombre": "Carlitros"}}
collection.update_many(myquery, newvalues)

'''
Actualizar un elemento de la colección

myquery = { "nombre": "Carlos" }
newvalues = { "$set": { "nombre": "Carlitros" } }

collection.update_one(myquery, newvalues)

'''

#Eliminar varios elementos de una colección (DELETE)
myquery2 = {"nombre": {"$regex": "Carlitros"}}
collection.delete_many(myquery2)

'''
-Eliminar un elemento de la colección

    myquery = { "nombre": "Carlos" }

    collection.delete_one(myquery)

-Eliminar todos los elemementos de la colección

    collection.delete_many({})

'''