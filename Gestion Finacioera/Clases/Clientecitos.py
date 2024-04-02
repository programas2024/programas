import tkinter as tk

class Clientesitos:
    def __init__(self, cliente_instance):
        self.cliente_instance = cliente_instance
        self.cambiar_colores()

    def limpiar_campos(self):
        self.cliente_instance.cedula_entry.delete(0, tk.END)
        self.cliente_instance.nombre_entry.delete(0, tk.END)
        self.cliente_instance.apellidos_entry.delete(0, tk.END)
        self.cliente_instance.telefono_entry.delete(0, tk.END)
        self.cliente_instance.email_entry.delete(0, tk.END)

    def cambiar_colores(self):
        self.cliente_instance.cambiar_color_cedula()
        self.cliente_instance.cambiar_color_nombre()
        self.cliente_instance.cambiar_color_apellidos()
        self.cliente_instance.cambiar_color_telefono()
        self.cliente_instance.cambiar_color_correo()
        self.cliente_instance.master.after(3000, self.cambiar_colores)