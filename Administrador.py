from Persona import Persona
class Administrador(Persona):
    def __init__(self, id, nombre, contrasena, correo):
        super().__init__(id, nombre, contrasena, correo)
    
    def agregarVuelo(self):
        pass

    def consultarVuelo(self):
        pass

