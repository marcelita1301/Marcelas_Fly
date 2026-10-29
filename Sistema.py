from  Vuelo import Vuelo
from Reserva import Reserva
from Usuario import Usuario
import ast

class Sistema():
    def __init__(self):
        self.__usuarios= []
        self.__vuelos= []
        self.__useract= any
        self.__reservas=[]

    def to_import_usuarios(self,file_name):
        try:
            out = open(file_name, "r")
            lineas= out.readlines()
            for i in lineas:
                l=i.split(",")
                self.agregar_usuario(Usuario(l[0],l[1],l[2],l[3],int(l[4])))
    
        except FileNotFoundError:
            print("El archivo no fue encontrado")
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            
    def to_file_usuarios(self,file_name):
        try:
            out = open(file_name, "w")
            for i in self.__usuarios:
                out.write(f"{i.__str__()}\n")
            out.close()
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")        

    def agregar_usuario(self, usuario):
        for u in self.__usuarios:
            if u.get_id() == usuario.get_id():
                 return None
        self.__usuarios.append(usuario)    
        return True
    def agregar_reserva(self,r):
        self.__reservas.append(r)

    def verificar_login(self, documento, contrasena):
        for u in self.__usuarios:
            if u.get_id() == documento and u.get_contrasena() == contrasena:
                return True
        return False

    def buscar_usuario(self, id):
        for u in self.__usuarios:
            if u.get_id() == id:
                return u
        return False

    def get_useract(self):
        return self.__useract
    def set_useract(self,u):
        self.__useract=u
    
    def agregarVuelo(self,vuelo):
        for v in self.__vuelos:
            if vuelo.get_codigo_vuelo() == v.get_codigo_vuelo():
                return False
        self.__vuelos.append(vuelo)
        return True
    
    def to_file_reservas(self,file_name):
        try:
            out = open(file_name, "w")
            for i in self.__usuarios:
                for j in i.get_reservas():
                    out.write(f"{j.__str__()}\n")
            out.close()
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
    
    def to_import_reservas(self,file_name):
        try:
            out = open(file_name, "r")
            lineas= out.readlines()
            for i in lineas:
                l=i.replace("\n","").split("-")  
                        
                pasajeros=ast.literal_eval(l[2])
                sillas=ast.literal_eval(l[3])
                user=self.buscar_usuario(l[0])
                reserva=Reserva(l[0],l[1],pasajeros,sillas,l[4],int(l[5]),l[6])
                user.agregar_reserva(reserva)   # type: ignore
                self.agregar_reserva(reserva) # type: ignore
            out.close()
            
        except FileNotFoundError:
            print("El archivo no fue encontrado")
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")



    def to_import_vuelos(self,file_name):
        try:
            out = open(file_name, "r")
            lineas= out.readlines()
            for i in lineas:
                l=i.split()
    

               
                cv=l[0]
                co=l[1]
                cd=l[2]
                dia=l[3]
                h=l[4]
                sp=l[5]
                se=l[6].replace("\n","")
                self.agregarVuelo(Vuelo(cv,co,cd,dia,h,sp,se))
                out.close()
        except FileNotFoundError:
            print("El archivo no fue encontrado")
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
    
    def to_file_vuelos(self,file_name):
        try:
            out = open(file_name, "w")
            for i in self.__vuelos:
                out.write(f"{i.__str__()}\n")
            out.close()
        except PermissionError:
            print("No se puede acceder al archivo")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")


    def get_vuelos(self):
        return self.__vuelos    
    def get_usuarios(self):
        return self.__usuarios
    def get_reservas(self):
        return self.__reservas