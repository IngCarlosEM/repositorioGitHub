class users():

    def __init__(self, nombre, a_paterno, a_materno, correo):
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.correo = correo

    def toDBCollection (self):
        return {
                "nombre": self.nombre,
                "a_paterno": self.a_paterno,
                "a_materno": self.a_materno,
                "correo": self.correo
            }   

    def __str__(self):
        return "Nombre: %s - a_paterno: %s - a_materno: %s - correo: %s" \
               %(self.nombre, self.a_paterno, self.a_materno, self.correo)