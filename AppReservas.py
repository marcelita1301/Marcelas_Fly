import tkinter as tk
from tkinter import ttk, messagebox

class AppReservas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Reservas")
        self.root.geometry("400x200")
        self.root.config(bg="white")

        # Lista de reservas simulada
        self.reservas = ["Reserva 101", "Reserva 102", "Reserva 103"]

        # Label
        tk.Label(root, text="Reservas disponibles:", bg="white", font=("Arial", 11)).pack(pady=10)

        # Combobox de reservas
        self.combo_reserva = ttk.Combobox(root, values=self.reservas, state="readonly", font=("Arial", 11))
        self.combo_reserva.pack(pady=5)

        # Botón para eliminar
        btn_eliminar = tk.Button(root, text="Eliminar reserva", command=self.eliminar_reserva, font=("Arial", 11))
        btn_eliminar.pack(pady=20)

    def eliminar_reserva(self):
        seleccion = self.combo_reserva.get()

        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una reserva.")
            return

        self.reservas.remove(seleccion)
        self.actualizar_combobox()
        messagebox.showinfo("Éxito", "Reserva eliminada correctamente.")

    def actualizar_combobox(self):
        self.combo_reserva['values'] = self.reservas
        self.combo_reserva.set("")

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = AppReservas(root)
    root.mainloop()