class Vuelo:
    def __init__(self,codigo_vuelo,ciudad_origen,destino,dia,horario,silla_preferencial,silla_economica):
        self.__codigo_vuelo = codigo_vuelo
        self.__ciudad_origen = ciudad_origen
        self.__destino = destino
        self.__dia=dia
        self.__horario = horario
        self.__silla_preferencial = silla_preferencial
        self.__silla_economica = silla_economica
    
    def get_codigo_vuelo(self):
        return self.__codigo_vuelo
        
    def get_ciudad_origen(self):
        return self.__ciudad_origen
    
    def get_dia(self):
        return self.__dia

    def get_destino(self):
        return self.__destino

    def get_horario(self):
        return self.__horario
        
    def get_silla_preferencial(self):
        return self.__silla_preferencial

    def get_silla_economica(self):
        return self.__silla_economica

    def set_codigo_vuelo(self,codigo_vuelo):
        self.__codigo_vuelo = codigo_vuelo
        
    def set_ciudad_origen(self,ciudad_origen):
        self.__ciudad_origen = ciudad_origen
    
    def set_dia(self,dia):
        self.__dia=dia

    def set_destino(self,destino):
        self.__destino = destino

    def set_horario(self,horario):
        self.__horario = horario
        
    def set_silla_preferencial(self,silla_preferencial):
        self.__silla_preferencial = silla_preferencial

    def set_silla_economica(self,silla_economica):
        self.__silla_economica = silla_economica
    
    def __str__(self):
        return self.__codigo_vuelo.upper()+" "+ self.__ciudad_origen+"	"+self.__destino+"	"+self.__dia+"  "+self.__horario+"	"+self.__silla_preferencial+"	"+self.__silla_economica
    