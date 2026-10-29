from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self,id,nombre,contrasena,correo):
        self.__id = id
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__correo = correo

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
    
    def get_contrasena(self):
        return self.__contrasena
    
    def get_correo(self):
        return self.__correo    

    def set_id(self,id):
        self.__id=id

    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def set_contrasena(self,c):
        self.__contrasena=c

    def set_correo(self,correo):
        self.__correo=correo
