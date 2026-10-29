from Persona import Persona
class Usuario(Persona):
    def __init__(self, id, nombre, contrasena, correo,millas=0):
        super().__init__(id, nombre, contrasena, correo)
        self.__millas=millas
        self.__reservas=[]
    
    def get_millas(self):
        return self.__millas
    
    def get_reservas(self):
        return self.__reservas

    def sumar_millas(self):
        self.__millas += 500
    def restar_millas(self):
        self.__millas -= 2000

    def agregar_reserva(self,r):
        self.__reservas.append(r)
        
    def buscar_reserva(self,numR):
        for i in self.__reservas:
            if i.get_num_reserva() == numR:
                return i
        else:
            return None
    def __str__(self):
        return (self.get_id()+","+ self.get_nombre()+","+self.get_contrasena()+","+self.get_correo())+","+str(self.__millas)
    
        