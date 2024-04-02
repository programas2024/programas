import tkinter as tk


class Regitro:
    def __init__(self, registrar_instance):
        self.registrar_instance = registrar_instance

    def limpiar_campos(self, campo_erroneo):
        if campo_erroneo == "Cédula":
            self.registrar_instance.cedula_entry.delete(0, tk.END)
        elif campo_erroneo == "Nombre":
            self.registrar_instance.nombre_entry.delete(0, tk.END)
        elif campo_erroneo == "Apellidos":
            self.registrar_instance.apellidos_entry.delete(0, tk.END)
        elif campo_erroneo == "País":
            self.registrar_instance.pais_entry.delete(0, tk.END)
        elif campo_erroneo == "Ciudad":
            self.registrar_instance.ciudad_entry.delete(0, tk.END)
        elif campo_erroneo == "Correo":
            self.registrar_instance.correo_entry.delete(0, tk.END)
        elif campo_erroneo == "Usuario":
            self.registrar_instance.usuario_entry.delete(0, tk.END)
        elif campo_erroneo == "Contraseña":
            self.registrar_instance.contrasena_entry.delete(0, tk.END)