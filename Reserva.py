import ast
class Reserva():
    def __init__(self,usuario ,num_reserva, pasajeros, sillas, vuelo,precio_total=0,check_in="False"):
        self.__usuario=usuario
        self.__num_reserva=num_reserva
        self.__pasajeros=pasajeros
        self.__sillas=sillas
        self.__vuelo=vuelo
        self.__precio_total=precio_total
        self.__check_in=check_in


    def Resumen(self):
        return ""
    def realizarCheckIn(self):
        self.__check_in="True"
    def get_usuario(self):
        return self.__usuario
    def get_num_reserva(self):
        return self.__num_reserva
    def get_pasajeros(self):
        return self.__pasajeros
    def get_sillas(self):
        return self.__sillas
    def get_vuelo(self):
        return self.__vuelo
    def get_precioTotal(self):
        return self.__precio_total
    def get_check_in(self):
        return self.__check_in
    
    #pasajero1: Solo el ID
    #pasajero2: Información completa
    def modif_pasajeros(self,pasajero1,pasajero2):
        for i in range(len(self.__pasajeros)):
            if pasajero1 == self.__pasajeros[i][0]:
                self.__pasajeros[i] = pasajero2
                return True
        return False
    def modif_sillas(self):
        pass
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def set_contrasena(self,c):
        self.__contrasena=c

    def set_correo(self,correo):
        self.__correo=correo
    
    def __str__(self):
        return self.__usuario+"-"+self.__num_reserva+"-"+str(self.__pasajeros)+"-"+str(self.__sillas)+"-"+self.__vuelo+"-"+str(self.__precio_total)+"-"+str(self.__check_in)