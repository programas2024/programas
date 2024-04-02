import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from Ingresar import Ingresar
from Corresponsal import Corresponsal
from Corresponsalinvitado import CorresponsalInvitado
from Registrarce import Registrarce
from Tooltip import Tooltip
import mysql.connector


class Loggin:


    def mostrar_menu_contextual(self, event):
        self.menu_contextual = tk.Menu(self.master, tearoff=False)
        self.menu_contextual.add_command(label="Pegar", command=self.pegar)
        self.menu_contextual.add_command(label="Copiar", command=self.copiar)
        self.menu_contextual.tk_popup(event.x_root, event.y_root)

    def copiar(self):
        texto_ingresado = self.contrasena_entry.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(texto_ingresado)


    def pegar(self):
        texto_pegado = self.master.clipboard_get()
        self.contrasena_entry.insert(tk.INSERT, texto_pegado)

    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Inicio de Sesión")
        self.master.geometry("600x450")
        self.master.configure(bg="white")

        self.imagen_contraseña = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\contrasena.gif")
        self.imagen_ingresar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\doble-a-la-derecha.gif")
        self.imagen_registrar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\anadir.gif")
        self.imagen_invitado = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\contacto.gif")
        self.imagen_salir = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\salida (2).gif")
        


        self.usuario_label = tk.Label(master,background="white", text="Usuario:")
        self.usuario_entry = tk.Entry(master)

        self.sesion_label = tk.Label(master,background="white", text="INICIO DE SESION")
        self.sesion_label.place(x=120, y=20)

        self.fecha_label = tk.Label(master, text="")
        self.hora_label = tk.Label(master, text="")
        self.actualizar_fecha_hora()

        self.ingresar_handler = Ingresar(master, self)

        self.contrasena_label = tk.Label(master,background="white", text="Contraseña:")
        self.contrasena_entry = tk.Entry(master, show="*")

        self.mostrar_contrasena_button = tk.Button(master,image=self.imagen_contraseña,background="white", text="Mostrar Contraseña", command=self.mostrar_contrasena)
        self.mostrar_contrasena_button.place(x=330 ,y=130, width=70)
        self.mostrar_contrasena_button.bind("<Enter>", self.mostrar_contrasena)
        self.mostrar_contrasena_button.bind("<Leave>", self.ocultar_contrasena)
        
        self.ingresar_button = tk.Button(master, text="Ingresar",background="white",image=self.imagen_ingresar, command=self.ingresar)
        self.ingresar_button.place(x=30, y=200, width=210)
        Tooltip(self.ingresar_button,"Entrar al sistema")

        self.registrar_button = tk.Button(master, text="Registrarse",background="white",image=self.imagen_registrar, command=self.registrar)
        self.registrar_button.place(x=260, y=200, width=210)
        Tooltip(self.registrar_button,"Resgistrar ")

        self.invitado_button = tk.Button(master, text="Ingresar como Invitado",background="white",image=self.imagen_invitado, command=self.invitado)
        self.invitado_button.place(x=30, y=250, width=210)
        Tooltip(self.invitado_button,"Ingresar invitado")

        self.salir_button = tk.Button(master, text="Salir",background="white",image=self.imagen_salir, command=self.salir)
        self.salir_button.place(x=260, y=250, width=210)
        Tooltip(self.salir_button,"Salir")

        self.usuario_label.place(x=15, y=100)
        self.usuario_entry.place(x=120, y=100, width=200)
        Tooltip(self.usuario_entry,"Digite el usuario")
        

        self.contrasena_label.place(x=15, y=130)
        self.contrasena_entry.place(x=120, y=130, width=200)
        Tooltip(self.contrasena_entry,"Digite su contraseña")
        self.contrasena_entry.bind("<Button-3>", self.mostrar_menu_contextual)


    def mostrar_contrasena(self, event=None):
        self.contrasena_entry.config(show="")
            
    def ocultar_contrasena(self, event=None):
        self.contrasena_entry.config(show="*")

    def limpiar_contraseña(self):
        self.contrasena_entry.delete(0, tk.END)

    def ingresar(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        try:
            # Establece la conexión con la base de datos
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )

            # Crea un cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            # Prepara la consulta SQL para seleccionar el usuario y la contraseña
            query = "SELECT usuario, contrasena FROM registros WHERE usuario = %s AND contrasena = %s"
            cursor.execute(query, (usuario, contrasena))

            # Obtiene el resultado de la consulta
            result = cursor.fetchone()

            # Cierra el cursor y la conexión
            cursor.close()
            connection.close()

            # Si se encontró un resultado, significa que el usuario y la contraseña coinciden
            if result:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
                # Aquí puedes realizar las acciones que deseas luego del inicio de sesión exitoso

                ventana_Corresponsal= tk.Toplevel(self.master)
                app_Corresponsal = Corresponsal(ventana_Corresponsal)

            else:
                messagebox.showerror("Inicio de Sesión", "Usuario o contraseña incorrectos")

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {error}")

       
    def registrar(self):
       ventana_Corresponsalinvitado= tk.Toplevel(self.master)
       app_Corresponsal = Registrarce(ventana_Corresponsalinvitado)
    def invitado(self):
        ventana_Corresponsalinvitado= tk.Toplevel(self.master)
        app_Corresponsal = CorresponsalInvitado(ventana_Corresponsalinvitado)

    def salir(self):
        # Lógica para el botón de salir
        self.master.destroy()

    def actualizar_fecha_hora(self):
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d")
        hora = ahora.strftime("%H:%M:%S")
        
        self.fecha_label.config(text="Fecha: " + fecha)
        self.hora_label.config(text="Hora: " + hora)

        self.master.after(1000, self.actualizar_fecha_hora)

# Crear la ventana principal
root = tk.Tk()
app = Loggin(root)

# Iniciar el bucle principal
root.mainloop()