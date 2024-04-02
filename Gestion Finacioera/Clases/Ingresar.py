
from tkinter import messagebox


class Ingresar:
    def __init__(self, master, loggin_instance):
        self.master = master
        self.loggin_instance = loggin_instance

        # Establecer usuario y contraseña de ejemplo
        self.usuario_correcto = "holis"
        self.contrasena_correcta = "paula"

    def verificar_ingreso(self, usuario, contrasena):
        if usuario == self.usuario_correcto and contrasena == self.contrasena_correcta:
            messagebox.showinfo("Ingreso Exitoso", "¡Bienvenido al sistema!")
        else:
            self.loggin_instance.limpiar_contraseña()