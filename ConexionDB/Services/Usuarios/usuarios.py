from Models.mongo_model import create, read, update, delete

#Crear funciones de (CRUD) los datos vienen del routes

class users():

    def __init__(self, datos):
        self.datos = datos

    def crear_documento (self):
        
        documento = {
                "nombre": self.datos['nombre'],
                "a_paterno": self.datos['a_paterno'],
                "a_materno": self.datos['a_materno'],
                "correo": f"{self.datos['nombre']}.{self.datos['a_paterno']}@totalplay.com.mx"
            }
        create(documento) 
        return {"mensaje":"Registro creado"}
    
    def buscar_documento (self):
        lista = []
        documentos = read()
        for doc in documentos:
            aux = {}
            aux['nombre'] = doc['nombre'] 
            aux['a_materno'] = doc['a_materno'] 
            aux['a_paterno'] = doc['a_paterno'] 
            lista.append(aux)
        return lista
    
    def actualizar_documento (self):

        documento = {
                "nombre": self.datos['nombre'],
                "a_paterno": self.datos['a_paterno'],
                "a_materno": self.datos['a_materno'],
                "correo": f"{self.datos['nombre']}.{self.datos['a_paterno']}@totalplay.com.mx"
            }
        update(documento)
        return{"mensaje":"Registro actualizado"}
    
    def borrar_documento (self):

        documento = {
                "nombre": self.datos['nombre'],
                "a_paterno": self.datos['a_paterno'],
                "a_materno": self.datos['a_materno'],
                "correo": f"{self.datos['nombre']}.{self.datos['a_paterno']}@totalplay.com.mx"
            }
        delete(documento)
        return{"mensaje":"Registro borrado"}

