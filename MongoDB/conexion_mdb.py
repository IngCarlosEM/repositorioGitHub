from pymongo import MongoClient
#Conexión con BD
client = MongoClient('localhost')

#Crear BD
db = client['prueba']
#Crear una nueva colección
col = db['personas']

#Ver las BD 
print(client.list_database_names())

#Ver las colecciones de la BD

print(db.list_collection_names())

#Agregar documento a la colección
col.insert_one({
    'Edad': 20,
    'nombre': 'Carlos',
    'intereses': ['Futbol', 'Programacion']
})

#Contar el numero de documentos dentro de la coleción
print(col.count_documents({}))

#Insertar varios documentos
col.insert_many([
    {
    'Edad': 28,
    'nombre': 'Carlos',
    'intereses': ['Pizza', 'Pokemon']
    },
    {
    'Edad': 25,
    'nombre': 'Andy',
    'intereses': ['Anime', 'Conciertos']
    },
    {
    'Edad': 63,
    'nombre': 'Sofia',
    'intereses': ['Musica', 'Cocina']
    },
    {
    'Edad': 85,
    'nombre': 'Sara',
    'intereses': ['Religion', 'Comida']
    }
])

#Hacer un query
for documento in col.find({}):
    print(documento)