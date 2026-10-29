import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
import re
from Persona import Persona
from Usuario import Usuario
from Sistema import Sistema
from Administrador import Administrador
from Reserva import Reserva

class Root():
    def __init__(self,sistema):
        self.__sistema= sistema
        self.__admin= Administrador("1040", "Admin Marcela'sFly","12345678","adminMF2025@gmail.com")
        self.window=tk.Tk()
        self.window.title("Marcela'sFly")
        self.window.geometry("300x200")
        self.__sistema.to_import_vuelos("vuelos.txt")
        self.__sistema.to_import_usuarios("LISTA_USUARIO.txt")
        self.__sistema.to_import_reservas("reservas.txt")
        self.iniciar() 
    
    def mostrar_popup_personalizado(self, titulo, mensaje):
        popup = tk.Toplevel(self.window)
        popup.title(titulo)
        popup.configure(bg="#f0f0f0")
        popup.resizable(False, False)

        tk.Label(popup, text=mensaje, font=("Arial", 12), bg="#f0f0f0", wraplength=280).pack(pady=20)
        tk.Button(popup, text="Aceptar", command=popup.destroy, bg="#007acc", fg="white", font=("Arial", 10), width=10).pack()
       
        popup.update_idletasks()

        ancho = popup.winfo_width()
        alto = popup.winfo_height()
        x = (popup.winfo_screenwidth() // 2) - (ancho // 2)
        y = (popup.winfo_screenheight() // 2) - (alto // 2)
        popup.geometry(f"+{x}+{y}")

        popup.grab_set()
        self.window.wait_window(popup)


    def iniciar(self):
        self.window.configure(bg="#f4f4f4")  
        self.window.title("Sistema de Reservas Marcela'sFly")

        contenedor = tk.Frame(self.window, bg="#f4f4f4", padx=30, pady=30)
        contenedor.pack(expand=True)

        titulo = tk.Label(contenedor,text="  Bienvenido a Marcela'sFly  ",font=("Segoe UI", 20, "bold"),bg="#f4f4f4",fg="#2c3e50")
        titulo.pack(pady=(0, 30))

        btn_login = tk.Button(contenedor,text="🔐 Iniciar Sesión",command=self.login,font=("Segoe UI", 12),bg="#2980b9",fg="white",activebackground="#3498db",relief="raised",width=25,height=2)
        btn_login.pack(pady=10)

        btn_registro = tk.Button(contenedor,text="📝 Registrarse",command=self.registro,font=("Segoe UI", 12),bg="#27ae60",fg="white",activebackground="#2ecc71",relief="raised",width=25,height=2)
        btn_registro.pack(pady=10)

        btn_salir = tk.Button(contenedor,text="❌ Salir",command=self.window.quit,font=("Segoe UI", 12),bg="#c0392b",fg="white",activebackground="#e74c3c",relief="raised",width=25,height=2)
        btn_salir.pack(pady=(10, 0))

        self.window.update_idletasks()
        ancho = self.window.winfo_reqwidth()
        alto = self.window.winfo_reqheight()
        pantalla_ancho = self.window.winfo_screenwidth()
        pantalla_alto = self.window.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.window.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.window.resizable(False, False)
        self.window.title("Marcela'sFly")
        self.window.mainloop()

    
    def menu_usuario(self,usuario_actual):
        ventana_user = tk.Toplevel(self.window)
        ventana_user.title("Menú de Usuario")
        ancho = 500
        alto = 400

        ancho_pantalla = ventana_user.winfo_screenwidth()
        alto_pantalla = ventana_user.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        ventana_user.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana_user.configure(bg="#f0f8ff")  

        titulo = tk.Label(ventana_user, text="Bienvenido al Sistema de Vuelos", font=("Segoe UI", 16, "bold"), bg="#f4f4f4", fg="#2c3e50")
        titulo.pack(pady=20)

        marco_botones = tk.Frame(ventana_user, bg="#f0f8ff")
        marco_botones.pack(pady=10)

        def cambiar_contrasena(usuario_actual):
            ventana_cambio = tk.Toplevel(self.window)
            ventana_cambio.title("Cambiar Contraseña")
            ventana_cambio.configure(bg="#f0f8ff")
            ventana_cambio.resizable(False, False)

            ancho = 400
            alto = 250
            x = (ventana_cambio.winfo_screenwidth() // 2) - (ancho // 2)
            y = (ventana_cambio.winfo_screenheight() // 2) - (alto // 2)
            ventana_cambio.geometry(f"{ancho}x{alto}+{x}+{y}")

            tk.Label(ventana_cambio, text="Cambiar Contraseña", font=("Segoe UI", 16, "bold"), bg="#f0f8ff").pack(pady=15)

            frame = tk.Frame(ventana_cambio, bg="#f0f8ff")
            frame.pack(pady=10)

            tk.Label(frame, text="Contraseña Actual:", bg="#f0f8ff", font=("Segoe UI", 12)).grid(row=0, column=0, pady=5, sticky="e")
            actual = tk.Entry(frame, show="*", font=("Segoe UI", 12))
            actual.grid(row=0, column=1, pady=5)

            tk.Label(frame, text="Nueva Contraseña:", bg="#f0f8ff", font=("Segoe UI", 12)).grid(row=1, column=0, pady=5, sticky="e")
            nueva = tk.Entry(frame, show="*", font=("Segoe UI", 12))
            nueva.grid(row=1, column=1, pady=5)

            tk.Label(frame, text="Confirmar Nueva:", bg="#f0f8ff", font=("Segoe UI", 12)).grid(row=2, column=0, pady=5, sticky="e")
            confirmar = tk.Entry(frame, show="*", font=("Segoe UI", 12))
            confirmar.grid(row=2, column=1, pady=5)

            def guardar_contraseña():
                actual_val = actual.get()
                nueva_val = nueva.get()
                confirmar_val = confirmar.get()

                if actual_val != usuario_actual.get_contrasena():
                    self.mostrar_popup_personalizado("Error", "La contraseña actual no es correcta")
                    return

                if nueva_val != confirmar_val:
                    self.mostrar_popup_personalizado("Error", "La nueva contraseña no coincide en ambas entradas")
                    return

                if len(nueva_val) < 8:
                    self.mostrar_popup_personalizado("Error", "La nueva contraseña debe tener al menos 8 caracteres")
                    return

                usuario_actual.set_contrasena(nueva_val)
                self.__sistema.to_file_usuarios("LISTA_USUARIO.txt")
                self.mostrar_popup_personalizado("Éxito", "Contraseña cambiada correctamente")
                ventana_cambio.destroy()

            tk.Button(ventana_cambio, text="Guardar", bg="#27ae60", fg="white", font=("Segoe UI", 12), command=guardar_contraseña).pack(pady=10)
        boton_cambiar_clave = tk.Button(marco_botones, text="🔐 Cambiar Contraseña", font=("Segoe UI", 12), width=18, bg="#f39c12", fg="white", activebackground="#f1c40f", relief="raised", command=lambda: cambiar_contrasena(usuario_actual))
        boton_cambiar_clave.grid(row=4, column=0, padx=10, pady=10)
    

        
        def check_in(usuario_actual):
            ventana_check = tk.Toplevel(self.window)
            ventana_check.title("Realizar Check-In")
            ventana_check.configure(bg="#f0f4f7")
            ancho = 720
            alto = 100

            ancho_pantalla = ventana_user.winfo_screenwidth()
            alto_pantalla = ventana_user.winfo_screenheight()

            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (alto_pantalla // 2) - (alto // 2)

            ventana_check.geometry(f"{ancho}x{alto}+{x}+{y}")
            
            tk.Label(ventana_check, text="Seleccione su número de reserva", font=("Helvetica", 14, "bold"), bg="#f0f4f7").grid(row=0, column=0, padx=10, pady=15, sticky="w")
            
            reservas = ttk.Combobox(ventana_check, font=("Helvetica", 12), width=25, values=[i.get_num_reserva() for i in usuario_actual.get_reservas() if i.get_check_in().replace("\n","") == "False"])
            reservas.grid(row=0, column=1, padx=10, pady=15)
            
            def check_in_reserva(usuario_actual):
                reserva=reservas.get()

                if not reserva:
                    self.mostrar_popup_personalizado("Advertencia","Debe seleccionar una reserva")
                else:
                    reserva_obj = next((r for r in self.__sistema.get_reservas() if r.get_num_reserva() == reserva), None)
                    if not reserva_obj:
                        self.mostrar_popup_personalizado("Error", "No se encontró la reserva")
                        return

                vuelo = next((v for v in self.__sistema.get_vuelos() if v.get_codigo_vuelo() == reserva_obj.get_vuelo()), None)
                if not vuelo:
                    self.mostrar_popup_personalizado("Error", "No se encontró el vuelo de la reserva")
                    return
                ventana_check.destroy()

                sillas_pref = sum(1 for s in reserva_obj.get_sillas() if s.startswith("PREF"))
                sillas_eco = sum(1 for s in reserva_obj.get_sillas() if s.startswith("ECO"))

                ventana = tk.Toplevel(self.window)
                ventana.title(f"Check-In - Reserva: {reserva}")
                ventana.configure(bg="#f8fbff")
                ancho = 500
                alto = 500

                ancho_pantalla = ventana_user.winfo_screenwidth()
                alto_pantalla = ventana_user.winfo_screenheight()

                x = (ancho_pantalla // 2) - (ancho // 2)
                y = (alto_pantalla // 2) - (alto // 2)
                ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

                tk.Label(ventana, text="INFORMACIÓN DEL VUELO", font=("Helvetica", 16, "bold"), bg="#f8fbff", fg="#0d47a1").pack(pady=10)

                info_text = (
                    f"✈️Vuelo: {vuelo.get_codigo_vuelo()}\n"
                    f"📍 Origen: {vuelo.get_ciudad_origen()}\n"
                    f"🎯 Destino: {vuelo.get_destino()}\n"
                    f"📅 Día: {vuelo.get_dia()}\n"
                    f"⏰ Hora: {vuelo.get_horario()}\n"
                    f"💺 Sillas Preferenciales: {sillas_pref}\n"
                    f"💺 Sillas Económicas: {sillas_eco}\n"
                    f"🌍 Millas acumuladas: {usuario_actual.get_millas()}"
                )
                tk.Label(ventana, text=info_text, font=("Helvetica", 12), bg="#f8fbff", justify="left").pack(pady=5)

                tk.Label(ventana, text="🧳 Gestión de maletas", font=("Helvetica", 14, "bold"), bg="#f8fbff", fg="#0d47a1").pack(pady=15)

                frame = tk.Frame(ventana, bg="#f8fbff")
                frame.pack(pady=5)

                tk.Label(frame, text="Tipo de maleta:", font=("Helvetica", 12), bg="#f8fbff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
                tipo_maleta = ttk.Combobox(frame, values=["Mano", "Cabina", "Bodega"], font=("Helvetica", 12), width=20)
                tipo_maleta.grid(row=0, column=1, pady=5)

                tk.Label(frame, text="Peso (kg):", font=("Helvetica", 12), bg="#f8fbff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
                peso_entry = tk.Entry(frame, font=("Helvetica", 12))
                peso_entry.grid(row=1, column=1, pady=5)

                costo_label = tk.Label(ventana, text="Costo acumulado: $0", font=("Helvetica", 12, "bold"), bg="#f8fbff", fg="#2e7d32")
                costo_label.pack(pady=10)

                maletas_mano = 0
                maletas_cabina = 0
                maletas_bodega = 0
                costo_total = 0

                def agregar_maleta():
                    nonlocal maletas_mano, maletas_cabina, maletas_bodega, costo_total

                    tipo = tipo_maleta.get()
                    try:
                        peso = float(peso_entry.get())
                    except ValueError:
                        self.mostrar_popup_personalizado("Error", "Peso inválido")
                        return

                    if tipo == "Mano":
                        if peso <=0:
                            self.mostrar_popup_personalizado("Error", "Debe ingresar pesos validos")
                            return
                        if peso > 10:
                            self.mostrar_popup_personalizado("Error", "Peso máximo de mano: 10 kg")
                            return
                        maletas_mano += 1
                        self.mostrar_popup_personalizado("Agregado", "Maleta de mano incluida sin costo.")
                        
                    elif tipo == "Cabina":
                        if peso <=0:
                            self.mostrar_popup_personalizado("Error", "Debe ingresar pesos validos")
                            return
                        if peso > 10:
                            self.mostrar_popup_personalizado("Error", "Peso máximo para cabina: 10 kg")
                            return
                        if sillas_pref > 0:
                            maletas_cabina += 1
                            self.mostrar_popup_personalizado("Agregado", "Maleta de cabina incluida sin costo (preferencial).")
                        else:
                            costo_total += 40000
                            maletas_cabina += 1
                            self.mostrar_popup_personalizado("Agregado", "Costo $40.000 agregado por maleta de cabina (económica).")
                    elif tipo == "Bodega":
                        if peso <=0:
                            self.mostrar_popup_personalizado("Error", "Debe ingresar pesos validos")
                            return
                        if maletas_bodega < sillas_pref:
                            maletas_bodega += 1
                            self.mostrar_popup_personalizado("Agregado", "Maleta de bodega incluida sin costo (preferencial).")
                        else:
                            extra = int(peso * 7000)
                            costo_total += extra
                            maletas_bodega += 1
                            self.mostrar_popup_personalizado("Agregado", f"Costo ${extra} agregado por maleta adicional de bodega.")
                    else:
                        self.mostrar_popup_personalizado("Error", "Seleccione un tipo de maleta válido.")
                        return

                    costo_label.config(text=f"Costo acumulado: ${costo_total}")

                    tipo_maleta.set("")
                    peso_entry.delete(0, tk.END)

                tk.Button(ventana, text="➕ Agregar maleta", command=agregar_maleta,font=("Helvetica", 12), bg="#2980b9", fg="white", activebackground="#2980b9").pack(pady=5)
                
                def finalizar_checkin():
                    
                    r=reserva_obj
                    user=self.__sistema.buscar_usuario(usuario_actual.get_id())
                    
                    user.buscar_reserva(r.get_num_reserva()).realizarCheckIn()
                    
                    self.__sistema.to_file_reservas("reservas.txt")
                    messagebox.showinfo(
                        "✅ Check-In completado",
                        f"Resumen:\n"
                        f"- Maletas de mano: {maletas_mano}\n"
                        f"- Maletas de cabina: {maletas_cabina}\n"
                        f"- Maletas de bodega: {maletas_bodega}\n"
                        f"- Costo total adicional: ${costo_total}"
                    )
                    ventana.destroy()

                tk.Button(ventana, text="✔ Finalizar Check-In", font=("Helvetica", 13, "bold"),bg="#27ae60", fg="white", activebackground="#27ae60", command=finalizar_checkin).pack(pady=10)
                    
            confirmar_vuelo = tk.Button(ventana_check, text="Confirmar", font=("Segoe UI", 12), bg="#27ae60", fg="white",activebackground="#388e3c", relief="raised", command=lambda: check_in_reserva(usuario_actual))
            confirmar_vuelo.grid(row=0, column=2, padx=10, pady=15)
        boton_checkin = tk.Button(marco_botones, text="🛄 Realizar Check-In", font=("Segoe UI", 12), width=18, bg="#2980b9", fg="white", activebackground="#2980b9", relief="raised", command=lambda: check_in(usuario_actual))
        boton_checkin.grid(row=1, column=0, padx=10, pady=10)

        def hacer_reserva(usuario_actual):
            ventana = tk.Toplevel(self.window)    
            ventana.title("Hacer Reserva de Vuelo")
            ancho = 1060
            alto = 600

            ancho_pantalla = ventana_user.winfo_screenwidth()
            alto_pantalla = ventana_user.winfo_screenheight()
            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (alto_pantalla // 2) - (alto // 2)
            ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
            ventana.configure(bg="white")

            style = ttk.Style()
            style.theme_use("clam")
            
            style.configure("Treeview",background="#ffffff",foreground="black",rowheight=28,fieldbackground="#ffffff",font=("Segoe UI", 11))
            style.configure("Treeview.Heading",font=("Segoe UI", 12, "bold"),background="#d9eaff",foreground="black")
            style.map("Treeview",background=[('selected', '#a3c9f1')],foreground=[('selected', 'black')])

            style.configure("TButton", font=("Segoe UI", 12), padding=6)

            frame_filtro = ttk.LabelFrame(ventana, text="Buscar vuelos", padding=10)
            frame_filtro.grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

            vuelos= self.__sistema.get_vuelos()

            lista_origen=list(map(lambda x:x.get_ciudad_origen(), vuelos))
            lista_destino=list(map(lambda x:x.get_destino(), vuelos))

            frame_filtro.columnconfigure((0, 1, 2, 3), weight=1)

            ttk.Label(frame_filtro, text="Origen:", font=("Segoe UI", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
            origen = ttk.Combobox(frame_filtro, font=("Segoe UI", 12), values=sorted(set(lista_origen)))
            origen.grid(row=0, column=1, padx=5, pady=5, sticky="w")

            ttk.Label(frame_filtro, text="Destino:", font=("Segoe UI", 12)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
            destino = ttk.Combobox(frame_filtro, font=("Segoe UI", 12), values=sorted(set(lista_destino)))
            destino.grid(row=0, column=3, padx=5, pady=5, sticky="w")

            frame_tabla = ttk.LabelFrame(ventana, text="Resultados", padding=10)
            frame_tabla.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

            tabla = ttk.Treeview(frame_tabla, columns=("codigo", "dia", "hora", "pref", "eco"), show="headings", height=6)
            tabla.heading("codigo", text="Código")
            tabla.heading("dia", text="Día")
            tabla.heading("hora", text="Hora")
            tabla.heading("pref", text="Pref.")
            tabla.heading("eco", text="Econ.")
            tabla.pack()

            def filtrar_vuelos():
                tabla.delete(*tabla.get_children())
                ori= origen.get().strip().upper()
                des= destino.get().strip().upper()

                if not ori or not des:
                    self.mostrar_popup_personalizado("Advertencia","Debe seleccionar origen y destino")
                    return
                for v in vuelos:
                    si_prt=int(v.get_silla_preferencial())
                    si_ect=int(v.get_silla_economica())
                    

                    for r in self.__sistema.get_reservas():
                        if v.get_codigo_vuelo()==r.get_vuelo():
                            for s in r.get_sillas():
                                if  s[0] == "P":
                                    si_prt-=1
                                else:
                                    si_ect-=1
                    if v.get_ciudad_origen() == ori and v.get_destino() == des:
                        tabla.insert("", "end", values=(
                            v.get_codigo_vuelo(),
                            v.get_dia(), 
                            v.get_horario(),
                            si_prt,
                            si_ect,       
                                    ))
            
            frame_filtro.grid_columnconfigure(0, weight=1)
            ttk.Button(frame_filtro, text="🔍 Buscar vuelos", command=filtrar_vuelos).grid(row=1, column=0, columnspan=4, pady=10)


            frame_sillas = ttk.LabelFrame(ventana, text="Seleccionar cantidad de sillas", padding=10)
            frame_sillas.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

            frame_sillas.columnconfigure((0, 1, 2, 3), weight=1)

            ttk.Label(frame_sillas, text="Sillas Preferenciales:", font=("Segoe UI", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
            pref = ttk.Entry(frame_sillas, font=("Segoe UI", 12), width=10)
            pref.grid(row=0, column=1, sticky="w")

            ttk.Label(frame_sillas, text="Sillas Económicas:", font=("Segoe UI", 12)).grid(row=0, column=2, padx=10, pady=5, sticky="e")
            econ = ttk.Entry(frame_sillas, font=("Segoe UI", 12), width=10)
            econ.grid(row=0, column=3, sticky="w")

 
            def confirmar_reserva():
                seleccionado= tabla.focus()
                if not seleccionado:
                    self.mostrar_popup_personalizado("Error","Debes seleccionar un vuelo")
                    return
                codigo=tabla.item(seleccionado)["values"][0]
                vuelo = next((v for v in vuelos if v.get_codigo_vuelo() == codigo),None)

                if vuelo is None:
                    self.mostrar_popup_personalizado("Error", "Vuelo no encontrado.")
                    return
                
                cant_eco=0
                cant_pref=0
                try:
                    cant_pref = int(pref.get()) if pref.get() else 0
                    cant_eco = int(econ.get()) if econ.get() else 0
                    if cant_eco + cant_pref == 0:
                        raise ValueError
                    if cant_eco + cant_pref > 3:
                        self.mostrar_popup_personalizado("Error", "La cantidad máxima de sillas que puede comprar son 3")
                        return
                except:
                    self.mostrar_popup_personalizado("Error", "Debe ingresar al menos una silla valida")
                    return
                
                total_sillas_compradas = cant_eco + cant_pref
                precio_total=0
                sillas=[]

                disponibles_eco = int(vuelo.get_silla_economica())
                disponibles_pref = int(vuelo.get_silla_preferencial())
                
                
                if cant_eco > 0: 
                    if cant_eco > disponibles_eco:
                        self.mostrar_popup_personalizado("Error", f"Sillas económicas disponibles: {disponibles_eco}")
                        return
                    precio_total += cant_eco * 235000
                    sillas.extend(["economica"] * cant_eco)
                
                if cant_pref > 0: 
                    cant_preft=cant_pref
                    cant_pref2=cant_pref
                    if cant_pref > disponibles_pref:
                        self.mostrar_popup_personalizado("Error", f"Sillas preferenciales disponibles: {disponibles_pref}")
                        return
                    if int(usuario_actual.get_millas())>=2000:
                        usuario_actual.restar_millas()
                        self.__sistema.to_file_usuarios("LISTA_USUARIO.txt")
                        precio_total+=235000
                        cant_pref2-=1
                        self.mostrar_popup_personalizado("Felicitaciones", f"¡Enhorabuena!, tuviste un descuento en una silla preferencial. Millas restantes: {usuario_actual.get_millas()}")
                    precio_total += cant_pref2 * 850000
                    sillas.extend(["preferencial"] * cant_preft)
                    
                def seleccionar_sillas(vuelo, cant_eco, cant_pref, confirmar_callback, sillas_anteriores=None):
                    ventana_sillas = tk.Toplevel()
                    ventana_sillas.title("Seleccionar sillas")
                    ventana_sillas.configure(bg="#f0f8ff")  
                    ventana_sillas.resizable(False, False)

                    sillas_seleccionadas = []
                    botones = {}

                    total_disponibles = int(vuelo.get_silla_economica()) + int(vuelo.get_silla_preferencial())
                    total_sillas = cant_eco + cant_pref

                    seleccion_eco = 0
                    seleccion_pref = 0

                    sillas_ocupadas = []
                    for reserva in self.__sistema.get_reservas():
                        if reserva.get_vuelo() == vuelo.get_codigo_vuelo():
                            sillas_ocupadas.extend(reserva.get_sillas())

                    if sillas_anteriores:
                        for silla in sillas_anteriores:
                            if silla in sillas_ocupadas:
                                sillas_ocupadas.remove(silla)

                    tk.Label(ventana_sillas, text="Seleccione sus sillas", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=15)

                    marco = tk.Frame(ventana_sillas, bg="#f0f8ff")
                    marco.pack()

                    filas = 10
                    columnas = total_disponibles // filas + 1
                    idx = 1

                    for r in range(filas):
                        for c in range(columnas):
                            if idx > total_disponibles:
                                break

                            if idx <= int(vuelo.get_silla_preferencial()):
                                tipo = "PREF"
                                color = "lightblue"
                            else:
                                tipo = "ECO"
                                color = "lightgreen"

                            etiqueta = f"{tipo}_{idx}" 
                            if etiqueta in sillas_ocupadas:
                                estado = "disabled"
                                color = "gray" 

                            def seleccionar(etiqueta=etiqueta, tipo=tipo):
                                nonlocal seleccion_eco, seleccion_pref

                                if etiqueta in sillas_seleccionadas:
                                    sillas_seleccionadas.remove(etiqueta)
                                    botones[etiqueta].config(relief="raised")
                                    if tipo == "ECO":
                                        seleccion_eco -= 1
                                    else:
                                        seleccion_pref -= 1
                                    return

                                if tipo == "ECO" and seleccion_eco >= cant_eco:
                                    self.mostrar_popup_personalizado("Límite alcanzado", f"Solo puedes seleccionar {cant_eco} silla(s) económica(s).")
                                    return
                                
                                elif tipo == "PREF" and seleccion_pref >= cant_pref:
                                    self.mostrar_popup_personalizado("Límite alcanzado", f"Solo puedes seleccionar {cant_pref} silla(s) preferencial(es).")
                                    return

                                sillas_seleccionadas.append(etiqueta)
                                botones[etiqueta].config(relief="sunken")
                                if tipo == "ECO":
                                    seleccion_eco += 1
                                else:
                                    seleccion_pref += 1

                            boton = tk.Button(marco,text=etiqueta, width=8, height=2, bg=color, font=("Arial", 10, "bold"),command=lambda e=etiqueta, t=tipo: seleccionar(e, t))
                            boton.grid(row=r, column=c, padx=5, pady=5)
                            botones[etiqueta] = boton

                            if etiqueta in sillas_ocupadas:
                                botones[etiqueta].config(state="disabled")
                            else:
                                botones[etiqueta].config(state="normal")
                            idx += 1


                    def confirmar_seleccion():
                        if len(sillas_seleccionadas) != total_sillas:
                            self.mostrar_popup_personalizado("Error", "Debes seleccionar exactamente las sillas que compraste.")
                            return
                        
                        if sillas_anteriores:
                            for silla in sillas_anteriores:
                                if silla.startswith("ECO"):
                                    vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) + 1))
                                elif silla.startswith("PREF"):
                                    vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) + 1))

                        vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) - seleccion_eco))
                        vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) - seleccion_pref))
                        self.__sistema.to_file_vuelos("vuelos.txt")
                        

                        ventana_sillas.destroy()
                        confirmar_callback(sillas_seleccionadas)
                    

                    tk.Button(ventana_sillas, text="Confirmar selección", font=("Helvetica", 13), bg="#2196f3", fg="white", padx=10, pady=5,command=lambda: confirmar_seleccion()).pack(pady=15)


                def seleccion(usuario_actual, vuelo, sillas_elegidas, precio_total):
                    pasajeros = [[usuario_actual.get_id(), usuario_actual.get_nombre()]]
                    
                    if len(sillas_elegidas) == 1:
                        self.finalizar_reserva(usuario_actual, vuelo, pasajeros, sillas_elegidas, precio_total)
                        ventana.destroy()
                        return

                    ventana_sel = tk.Toplevel(self.window)
                    ventana_sel.title("Agregar pasajeros")
                    ventana_sel.configure(bg="#f0f8ff")
                    ventana_sel.resizable(False, False)
                    ancho = 620
                    alto = 200
                    ancho_pantalla = ventana_user.winfo_screenwidth()
                    alto_pantalla = ventana_user.winfo_screenheight()

                    x = (ancho_pantalla // 2) - (ancho // 2)
                    y = (alto_pantalla // 2) - (alto // 2)

                    ventana_sel.geometry(f"{ancho}x{alto}+{x}+{y}")
                    
                    tk.Label(ventana_sel,text="Agregar pasajero adicional",font=("Helvetica", 16, "bold"),bg="#f0f8ff",fg="#003366").grid(row=0, column=0, columnspan=4, pady=(20, 10))

                    tk.Label(ventana_sel, text="Documento:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
                    documento = tk.Entry(ventana_sel, font=("Arial", 12), width=20)
                    documento.grid(row=1, column=1, padx=10, pady=10)

                    tk.Label(ventana_sel, text="Nombre:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=2, padx=10, pady=10, sticky="e")
                    nombre = tk.Entry(ventana_sel, font=("Arial", 12), width=20)
                    nombre.grid(row=1, column=3, padx=10, pady=10)

                    def agregar_pasajeros():
                        doc = documento.get().strip()
                        nom = nombre.get().strip()
                        if not doc or not nom:
                            self.mostrar_popup_personalizado("Error", "Debe ingresar nombre y documento.")
                            return
                        elif not doc.isdigit():
                            self.mostrar_popup_personalizado("Error", "Documento inválido")
                            return
                        elif nom.isdigit():
                            self.mostrar_popup_personalizado("Error","Nombre inválido")
                            return

                        pasajeros.append([doc, nom])
                        self.mostrar_popup_personalizado("Pasajero agregado", f"{nom} agregado correctamente como pasajero.")
                        documento.delete(0, tk.END)
                        nombre.delete(0, tk.END)

                        if len(pasajeros) == len(sillas_elegidas):
                            ventana_sel.destroy()
                            ventana.destroy()
                            self.finalizar_reserva(usuario_actual, vuelo, pasajeros, sillas_elegidas, precio_total) 

                    boton_agregar = tk.Button(ventana_sel,text="Agregar pasajero",font=("Helvetica", 12, "bold"),bg="#2196f3",fg="white",padx=15,pady=5,command=agregar_pasajeros)
                    boton_agregar.grid(row=2, column=0, columnspan=4, pady=(10, 20))
                     
                seleccionar_sillas(vuelo, cant_eco, cant_pref, lambda sillas_elegidas: seleccion(usuario_actual, vuelo, sillas_elegidas, int(precio_total))) 
            
            
            ttk.Button(ventana, text="✅ Confirmar Reserva", command=confirmar_reserva).grid(row=3, column=0, columnspan=4, pady=20)     
            
        boton_reserva = tk.Button(marco_botones, text="✈ Hacer reserva", font=("Segoe UI", 12), width=18, bg="#27ae60", fg="white", activebackground="#27ae60", relief="raised", command=lambda: hacer_reserva(usuario_actual))
        boton_reserva.grid(row=0, column=0, padx=10, pady=10)

        def modificar_reserva(usuario_actual):
            ventana_modificar = tk.Toplevel(self.window)
            ventana_modificar.title("Modificar Reserva")

            ancho = 600
            alto = 250
            ancho_pantalla = ventana_user.winfo_screenwidth()
            alto_pantalla = ventana_user.winfo_screenheight()
            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (alto_pantalla // 2) - (alto // 2)

            ventana_modificar.geometry(f"{ancho}x{alto}+{x}+{y}")
            ventana_modificar.configure(bg="#f0f8ff")

            frame_principal = tk.Frame(ventana_modificar, bg="#f0f8ff", padx=20, pady=20)
            frame_principal.pack(expand=True, fill="both")

            tk.Label(frame_principal, text="Seleccione una reserva:", font=("Arial", 14), bg="#f0f8ff", fg="#003366").pack(anchor="w")

            combo_reservas = ttk.Combobox(frame_principal, font=("Arial", 12),values=[r.get_num_reserva() for r in usuario_actual.get_reservas() if r.get_check_in().replace("\n","") == "False"])
            combo_reservas.pack(pady=10, fill="x")

            def seleccionar_sillas(vuelo, cant_eco, cant_pref, confirmar_callback, sillas_anteriores=None):
                ventana_sillas = tk.Toplevel()
                ventana_sillas.title("Seleccionar sillas")
                ventana_sillas.configure(bg="#f0f8ff")  
                ventana_sillas.resizable(False, False)

                sillas_seleccionadas = []
                botones = {}

                total_disponibles = int(vuelo.get_silla_economica()) + int(vuelo.get_silla_preferencial())
                total_sillas = cant_eco + cant_pref

                seleccion_eco = 0
                seleccion_pref = 0

                sillas_ocupadas = []
                for reserva in self.__sistema.get_reservas():
                    if reserva.get_vuelo() == vuelo.get_codigo_vuelo():
                        sillas_ocupadas.extend(reserva.get_sillas())

                if sillas_anteriores:
                    for silla in sillas_anteriores:
                        if silla in sillas_ocupadas:
                            sillas_ocupadas.remove(silla)

                tk.Label(ventana_sillas, text="Seleccione sus sillas", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=15)

                marco = tk.Frame(ventana_sillas, bg="#f0f8ff")
                marco.pack()

                filas = 10
                columnas = total_disponibles // filas + 1
                idx = 1

                for r in range(filas):
                    for c in range(columnas):
                        if idx > total_disponibles:
                            break

                        if idx <= int(vuelo.get_silla_preferencial()):
                            tipo = "PREF"
                            color = "lightblue"
                        else:
                            tipo = "ECO"
                            color = "lightgreen"

                        etiqueta = f"{tipo}_{idx}" 
                        if etiqueta in sillas_ocupadas:
                            estado = "disabled"
                            color = "gray" 

                        def seleccionar(etiqueta=etiqueta, tipo=tipo):
                            nonlocal seleccion_eco, seleccion_pref

                            if etiqueta in sillas_seleccionadas:
                                sillas_seleccionadas.remove(etiqueta)
                                botones[etiqueta].config(relief="raised")
                                if tipo == "ECO":
                                    seleccion_eco -= 1
                                else:
                                    seleccion_pref -= 1
                                return

                            if tipo == "ECO" and seleccion_eco >= cant_eco:
                                self.mostrar_popup_personalizado("Límite alcanzado", f"Solo puedes seleccionar {cant_eco} silla(s) económica(s).")
                                return
                            elif tipo == "PREF" and seleccion_pref >= cant_pref:
                                self.mostrar_popup_personalizado("Límite alcanzado", f"Solo puedes seleccionar {cant_pref} silla(s) preferencial(es).")
                                return

                            sillas_seleccionadas.append(etiqueta)
                            botones[etiqueta].config(relief="sunken")
                            if tipo == "ECO":
                                seleccion_eco += 1
                            else:
                                seleccion_pref += 1

                        boton = tk.Button(marco,text=etiqueta, width=8, height=2, bg=color, font=("Arial", 10, "bold"),command=lambda e=etiqueta, t=tipo: seleccionar(e, t))
                        boton.grid(row=r, column=c, padx=5, pady=5)
                        botones[etiqueta] = boton

                        if etiqueta in sillas_ocupadas:
                            botones[etiqueta].config(state="disabled")
                        else:
                            botones[etiqueta].config(state="normal")
                        idx += 1


                def confirmar_seleccion():
                    if len(sillas_seleccionadas) != total_sillas:
                        self.mostrar_popup_personalizado("Error", "Debes seleccionar exactamente las sillas que compraste.")
                        return
                    
                    if sillas_anteriores:
                        for silla in sillas_anteriores:
                            if silla.startswith("ECO"):
                                vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) + 1))
                            elif silla.startswith("PREF"):
                                vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) + 1))

                    vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) - seleccion_eco))
                    vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) - seleccion_pref))
                    self.__sistema.to_file_vuelos("vuelos.txt")
                    

                    ventana_sillas.destroy()
                    confirmar_callback(sillas_seleccionadas)
                

                tk.Button(ventana_sillas, text="Confirmar selección", font=("Helvetica", 13), bg="#2196f3", fg="white", padx=10, pady=5,command=lambda: confirmar_seleccion()).pack(pady=15)


            def mostrar_info():
                num_reserva = combo_reservas.get()
                reserva = next((r for r in usuario_actual.get_reservas() if r.get_num_reserva() == num_reserva), None)
                if not reserva:
                    messagebox.showerror("Error", "Reserva no encontrada")
                    return

                ventana_info = tk.Toplevel(ventana_modificar)
                ventana_info.title(f"Modificar Reserva {num_reserva}")
                ancho = 600
                alto = 300

                ancho_pantalla = ventana_info.winfo_screenwidth()
                alto_pantalla = ventana_info.winfo_screenheight()

                x = (ancho_pantalla // 2) - (ancho // 2)
                y = (alto_pantalla // 2) - (alto // 2)

                ventana_info.geometry(f"{ancho}x{alto}+{x}+{y}")

                ventana_info.configure(bg="#f9fbfd")

                frame_info = tk.Frame(ventana_info, bg="#f9fbfd", padx=20, pady=20)
                frame_info.pack(expand=True, fill="both")

                tk.Label(frame_info, text="Pasajeros actuales:", font=("Arial", 13, "bold"), bg="#f9fbfd").pack(anchor="w")
                for p in reserva.get_pasajeros():
                    tk.Label(frame_info, text=f"- {p[0]} - {p[1]}", font=("Arial", 11), bg="#f9fbfd").pack(anchor="w")

                tk.Label(frame_info, text=f"Sillas actuales: {', '.join(reserva.get_sillas())}",
                        font=("Arial", 12), bg="#f9fbfd").pack(pady=10, anchor="w")

                frame_botones = tk.Frame(frame_info, bg="#f9fbfd", pady=10)
                frame_botones.pack()

                def modificar_pasajeros():
                    ventana_p = tk.Toplevel(ventana_info)
                    ventana_p.title("Modificar Pasajeros")
                    ventana_p.geometry("400x250")
                    ventana_p.configure(bg="#ffffff")

                    tk.Label(ventana_p, text="Documento a cambiar").pack()
                    doc_ant = tk.Entry(ventana_p)
                    doc_ant.pack()

                    tk.Label(ventana_p, text="Nuevo documento").pack()
                    doc_nuevo = tk.Entry(ventana_p)
                    doc_nuevo.pack()

                    tk.Label(ventana_p, text="Nuevo nombre").pack()
                    nom_nuevo = tk.Entry(ventana_p)
                    nom_nuevo.pack()

                    def guardar():
                        ok = reserva.modif_pasajeros(doc_ant.get(), [doc_nuevo.get(), nom_nuevo.get()])
                        if ok:
                            self.__sistema.to_file_reservas("reservas.txt")
                            self.__sistema.to_file_usuarios("LISTA_USUARIO.txt")
                            self.mostrar_popup_personalizado("Éxito", "Pasajero actualizado")
                            ventana_p.destroy()
                        else:
                            self.mostrar_popup_personalizado("Error", "Pasajero no encontrado")

                    tk.Button(ventana_p, text="Guardar", command=guardar, bg="green", fg="white").pack(pady=10)
                tk.Button(frame_botones, text="Modificar Pasajeros", command=modificar_pasajeros,bg="orange", fg="white", padx=10).pack(side="left", padx=10)

                def modificar_sillas():
                    vuelo = next((v for v in self.__sistema.get_vuelos() if v.get_codigo_vuelo() == reserva.get_vuelo()), None)
                    if not vuelo:
                        self.mostrar_popup_personalizado("Error", "Vuelo no encontrado")
                        return

                    cant_eco = sum(1 for s in reserva.get_sillas() if s.startswith("ECO"))
                    cant_pref = sum(1 for s in reserva.get_sillas() if s.startswith("PREF"))

                    vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) + cant_eco))
                    vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) + cant_pref))

                    def confirmar_nueva_seleccion(sillas_nuevas):
                        reserva.get_sillas().clear()
                        reserva.get_sillas().extend(sillas_nuevas)

                        vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) - cant_eco))
                        vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) - cant_pref))

                        self.__sistema.to_file_reservas("reservas.txt")
                        self.__sistema.to_file_vuelos("vuelos.txt")
                        self.mostrar_popup_personalizado("Sillas modificadas", "Sillas cambiadas correctamente")
                        ventana_info.destroy()

                    seleccionar_sillas(vuelo, cant_eco, cant_pref, confirmar_nueva_seleccion, reserva.get_sillas())
                tk.Button(frame_botones, text="Modificar Sillas", command=modificar_sillas,bg="lightblue", fg="black", padx=10).pack(side="left", padx=10)

                def cancelar_reserva():
                    confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de cancelar esta reserva?")
                    if confirm:
                        vuelo = next((v for v in self.__sistema.get_vuelos() if v.get_codigo_vuelo() == reserva.get_vuelo()), None)
                        if vuelo:
                            cant_eco = sum(1 for s in reserva.get_sillas() if s.startswith("ECO"))
                            cant_pref = sum(1 for s in reserva.get_sillas() if s.startswith("PREF"))
                            vuelo.set_silla_economica(str(int(vuelo.get_silla_economica()) + cant_eco))
                            vuelo.set_silla_preferencial(str(int(vuelo.get_silla_preferencial()) + cant_pref))
                        usuario_actual.get_reservas().remove(reserva)
                        self.__sistema.get_reservas().remove(reserva)
                        self.__sistema.to_file_reservas("reservas.txt")
                        self.__sistema.to_file_vuelos("vuelos.txt")
                        self.__sistema.to_file_usuarios("LISTA_USUARIO.txt")
                        messagebox.showinfo("Cancelado", "Reserva eliminada correctamente")
                        ventana_info.destroy()
                
                tk.Button(frame_botones, text="Cancelar Reserva", command=cancelar_reserva,bg="red", fg="white", padx=10).pack(side="left", padx=10)
            
            tk.Button(frame_principal, text="Ver Detalles", font=("Arial", 12),command=mostrar_info, bg="#4caf50", fg="white", width=20).pack(pady=20)
        
        boton_modificar = tk.Button(marco_botones, text="📝 Modificar Reserva", font=("Segoe UI", 12), width=18, bg="#c0392b", fg="white", activebackground="#2980b9", relief="raised", command=lambda: modificar_reserva(usuario_actual))
        boton_modificar.grid(row=3, column=0, padx=10, pady=10)

        boton_cerrar_sesion = tk.Button(marco_botones, text="🚪 Cerrar Sesión", font=("Segoe UI", 12), width=18, bg="#27ae60", fg="white", activebackground="#27ae60", relief="raised", command=ventana_user.destroy)
        boton_cerrar_sesion.grid(row=5, column=0, padx=10, pady=10)


      
    def finalizar_reserva(self, usuario_actual, vuelo, pasajeros, sillas_elegidas, precio_total):
        numero = f"RSV{len(self.__sistema.get_reservas()) + 1:05d}"
        nueva_reserva = Reserva(usuario_actual.get_id(), numero,  pasajeros, sillas_elegidas, vuelo.get_codigo_vuelo(), precio_total)
        usuario_actual.agregar_reserva(nueva_reserva)
        usuario_actual.sumar_millas()
        self.__sistema.agregar_reserva(nueva_reserva)
        self.__sistema.to_file_reservas("reservas.txt")
        self.mostrar_popup_personalizado("Reserva exitosa", f"Reserva {numero} guardada correctamente. \nEl precio total de su compra es de: ${precio_total}")       

    def menu_admin(self):
        ventana_admin = tk.Toplevel(self.window)
        ventana_admin.title("Menú Administrador")
        ventana_admin.configure(bg="#f0f4f8")

        w, h = 400, 200
        x = ventana_admin.winfo_screenwidth() // 2 - w // 2
        y = ventana_admin.winfo_screenheight() // 2 - h // 2
        ventana_admin.geometry(f"{w}x{h}+{x}+{y}")

        label_titulo = tk.Label(ventana_admin, text="Menú del Administrador", font=("Segoe UI", 16, "bold"), bg="#f0f4f8")
        label_titulo.pack(pady=20)

        def agregar_vuelo():
            ventana_agregar = tk.Toplevel(ventana_admin)
            ventana_agregar.title("Agregar Nuevo Vuelo")
            ventana_agregar.configure(bg="#ffffff")

            w2, h2 = 500, 400
            x2 = ventana_agregar.winfo_screenwidth() // 2 - w2 // 2
            y2 = ventana_agregar.winfo_screenheight() // 2 - h2 // 2
            ventana_agregar.geometry(f"{w2}x{h2}+{x2}+{y2}")

            contenedor = tk.Frame(ventana_agregar, bg="white")
            contenedor.pack(padx=20, pady=20)

            campos = {
                "Código vuelo": tk.Entry(contenedor),
                "Ciudad Origen": tk.Entry(contenedor),
                "Día": tk.Entry(contenedor),
                "Destino": tk.Entry(contenedor),
                "Horario": tk.Entry(contenedor),
                "Sillas Preferenciales": tk.Entry(contenedor),
                "Sillas Económicas": tk.Entry(contenedor),
            }

            for i, (texto, entry) in enumerate(campos.items()):
                tk.Label(contenedor, text=texto + ":", font=("Segoe UI", 10), bg="white").grid(row=i, column=0, sticky="e", padx=10, pady=6)
                entry.grid(row=i, column=1, padx=10, pady=6)

            def guardar():
                codigo = campos["Código vuelo"].get().strip()
                origen = campos["Ciudad Origen"].get().strip()
                destino = campos["Destino"].get().strip()
                dia = campos["Día"].get().strip()
                horario = campos["Horario"].get().strip()
                sillas_pref_str = campos["Sillas Preferenciales"].get().strip()
                sillas_econ_str = campos["Sillas Económicas"].get().strip()

                if not all([codigo, origen, destino, dia, horario, sillas_pref_str, sillas_econ_str]):
                    self.mostrar_popup_personalizado("Error", "Todos los campos deben estar llenos")
                    return

                if any(char.isdigit() for char in origen) or any(char.isdigit() for char in destino):
                    self.mostrar_popup_personalizado("Error", "Las ciudades de origen y destino no deben contener números")
                    return
                
                if any(char.isdigit() for char in dia):
                    self.mostrar_popup_personalizado("Error", "El dia debe ser un dia de la semana")
                    return

                if any(char.isalpha() for char in horario):
                    self.mostrar_popup_personalizado("Error", "El horario no debe contener letras")
                    return

                try:
                    sillas_pref = int(sillas_pref_str)
                    sillas_econ = int(sillas_econ_str)
                    if sillas_pref < 0 or sillas_econ < 0:
                        raise ValueError
                except ValueError:
                    self.mostrar_popup_personalizado("Error", "Las sillas deben ser números enteros positivos")
                    return

                from Vuelo import Vuelo
                vuelo_nuevo = Vuelo(
                    codigo.upper(), origen.upper(), destino.upper(),
                    dia.upper(), horario, str(sillas_pref), str(sillas_econ)
                )
                self.__sistema.agregarVuelo(vuelo_nuevo)
                self.__sistema.to_file_vuelos("vuelos.txt")
                self.mostrar_popup_personalizado("Éxito", f"Vuelo {codigo.upper()} ha sido agregado")
                ventana_agregar.destroy()


            boton_guardar = tk.Button(contenedor, text="Guardar Vuelo", font=("Segoe UI", 10), bg="#4caf50", fg="white", command=guardar)
            boton_guardar.grid(row=len(campos), column=0, columnspan=2, pady=15)

        boton_agregar = tk.Button(ventana_admin, text="Agregar nuevo vuelo", font=("Segoe UI", 11), bg="#2196f3", fg="white", command=agregar_vuelo)
        boton_agregar.pack(pady=10)

        def consultar_vuelos():
            ventana_consulta = tk.Toplevel(ventana_admin)
            ventana_consulta.title("Consulta de Vuelos")
            ventana_consulta.configure(bg="#ffffff")

            w, h = 650, 400
            x = ventana_consulta.winfo_screenwidth() // 2 - w // 2
            y = ventana_consulta.winfo_screenheight() // 2 - h // 2
            ventana_consulta.geometry(f"{w}x{h}+{x}+{y}")

            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview", background="#f0f8ff", foreground="black", rowheight=25, fieldbackground="#f0f8ff", font=("Segoe UI", 10))
            style.map("Treeview", background=[("selected", "#b3d9ff")])

            tabla = ttk.Treeview(
                ventana_consulta,
                columns=("codigo", "vendidas", "pasajeros"),
                show="headings"
            )
            tabla.heading("codigo", text="Código Vuelo")
            tabla.heading("vendidas", text="Sillas Vendidas")
            tabla.heading("pasajeros", text="Pasajeros")
            tabla.pack(padx=20, pady=20, expand=True, fill="both")

            for reserva in self.__sistema.get_reservas():
                codigo = reserva.get_vuelo()
                sillas_vendidas = len(reserva.get_sillas())
                pasajeros = ", ".join([p[1] for p in reserva.get_pasajeros()])
                tabla.insert("", "end", values=(codigo, sillas_vendidas, pasajeros))
        
        boton_consultar = tk.Button(ventana_admin, text="Consultar Vuelos", font=("Segoe UI", 11), bg="#ff9800", fg="white", command=consultar_vuelos)
        boton_consultar.pack(pady=10)

    def login(self):
        ventana = tk.Toplevel(self.window)
        ventana.configure(bg="#f4f4f4")
        ventana.title("Iniciar sesión")

        contenedor = tk.Frame(ventana, bg="#f4f4f4", padx=30, pady=30)
        contenedor.pack(expand=True)

        tk.Label(contenedor, text="🔐 Bienvenido al sistema de reservas", font=("Segoe UI", 14, "bold"), bg="#f4f4f4", fg="#2c3e50").pack(pady=(0, 20))

        tk.Label(contenedor, text="🆔 Documento", font=("Segoe UI", 12), bg="#f4f4f4").pack(anchor="w")
        documento = tk.Entry(contenedor, font=("Segoe UI", 11), width=30)
        documento.pack(pady=(0, 10))

        tk.Label(contenedor, text="🔒 Contraseña", font=("Segoe UI", 12), bg="#f4f4f4").pack(anchor="w")
        contrasena = tk.Entry(contenedor, show="*", font=("Segoe UI", 11), width=30)
        contrasena.pack(pady=(0, 10))

        def logear():
            documento1 = documento.get()
            contrasena1 = contrasena.get()
            if documento1 == self.__admin.get_id() and contrasena1 == self.__admin.get_contrasena():
                self.mostrar_popup_personalizado("Bienvenido", f"Bienvenido {self.__admin.get_nombre()}")
                self.menu_admin()
                ventana.destroy()
            else:
                usuario = self.__sistema.verificar_login(documento1, contrasena1)
                if usuario is True:
                    usuario_actual = self.__sistema.buscar_usuario(documento1)
                    self.mostrar_popup_personalizado("Bienvenido", f"Bienvenido al sistema de reservas {usuario_actual.get_nombre()}")
                    self.__sistema.set_useract(usuario_actual)
                    self.menu_usuario(usuario_actual)
                    ventana.destroy()
                else:
                    self.mostrar_popup_personalizado("Error", "Documento o contraseña inválidos")

        tk.Button(contenedor,text="Iniciar Sesión",command=logear,font=("Segoe UI", 11),bg="#2980b9",fg="white",activebackground="#3498db",relief="raised",width=25,height=2).pack(pady=15)

        ventana.update_idletasks()
        w, h = ventana.winfo_reqwidth(), ventana.winfo_reqheight()
        sw, sh = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
        ventana.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")
        ventana.resizable(False, False)


    def registro(self):
        ventana = tk.Toplevel(self.window)
        ventana.configure(bg="#f4f4f4")
        ventana.title("Registro de usuario")

        contenedor = tk.Frame(ventana, bg="#f4f4f4", padx=30, pady=30)
        contenedor.pack(expand=True)

        tk.Label(contenedor, text="🧾 Formulario de Registro", font=("Segoe UI", 14, "bold"), bg="#f4f4f4", fg="#2c3e50").pack(pady=(0, 20))

        def campo_etiqueta(texto, icono=""):
            tk.Label(contenedor, text=f"{icono} {texto}", font=("Segoe UI", 12), bg="#f4f4f4").pack(anchor="w")

        def crear_entry(icono="", show=None):
            entry = tk.Entry(contenedor, font=("Segoe UI", 11), width=30, show=show)
            entry.pack(pady=(0, 10))
            return entry

        campo_etiqueta("Documento", "🆔")
        documento = crear_entry()

        campo_etiqueta("Nombre", "👤")
        nombre = crear_entry()

        campo_etiqueta("Correo", "📧")
        correo = crear_entry()

        campo_etiqueta("Contraseña", "🔒")
        contrasena = crear_entry(show="*")

        campo_etiqueta("Confirmar contraseña", "✅")
        contrasena_con = crear_entry(show="*")

        def confirmar():
            documento1 = documento.get()
            nombre1 = nombre.get()
            contrasena1 = contrasena.get()
            contrasena2 = contrasena_con.get()
            correo1 = correo.get()

            if not nombre1 or not correo1 or not documento1 or not contrasena1 or not contrasena2:
                self.mostrar_popup_personalizado("Error", "Todos los campos son obligatorios")
                return
            elif not documento1.isdigit():
                self.mostrar_popup_personalizado("Error", "Documento inválido")
                return
            elif nombre1.isdigit():
                self.mostrar_popup_personalizado("Error", "Nombre inválido")
                return
            elif not re.fullmatch(r"\S+@\S+\.\S+", correo1):
                self.mostrar_popup_personalizado("Error", "Correo mal estructurado")
                return
            elif len(contrasena1) < 8:
                self.mostrar_popup_personalizado("Error", "La contraseña tiene menos de 8 caracteres")
                return
            elif contrasena1 != contrasena2:
                self.mostrar_popup_personalizado("Error", "Las contraseñas no coinciden")
                return

            for u in self.__sistema.get_usuarios():
                if documento1 == u.get_id():
                    self.mostrar_popup_personalizado("Error", "El documento ya ha sido ingresado")
                    return
            else:
                nuevo_usuario = Usuario(documento1, nombre1, contrasena1, correo1)
                self.__sistema.agregar_usuario(nuevo_usuario)
                self.__sistema.to_file_usuarios("LISTA_USUARIO.txt")
                self.mostrar_popup_personalizado("Usuario registrado correctamente", f"Registrado {nombre1}")
                ventana.destroy()

        tk.Button(contenedor,text="✅ Registrar",font=("Segoe UI", 11),bg="#27ae60",fg="white",activebackground="#2ecc71",relief="flat",width=25,height=2,command=confirmar).pack(pady=15)

        ventana.update_idletasks()
        w, h = ventana.winfo_reqwidth(), ventana.winfo_reqheight()
        sw, sh = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
        ventana.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")
        ventana.resizable(False, False)
        
s1=Sistema()
r1=Root(s1)