from pymongo import MongoClient
#Conexión con BD
client = MongoClient('mongodb://localhost:27017/')
#Crear BD
db = client['prueba2']

#Ver las BD 
print(client.list_database_names())

#Crear una nueva colección
col = db['personas']

#Agregar documento a la colección
col.insert_one({
    'nombre': 'Carlos',
    'correo': 'carlos.esparzam@totalplay.com'
})

#Ver las colecciones de la BD
print(db.list_collection_names())

#Hacer un query
for documento in col.find({}):
    print(documento)