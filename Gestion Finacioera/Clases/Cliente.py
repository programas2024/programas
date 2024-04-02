import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

class Cliente:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Clientes")
        self.master.geometry("400x300")
        self.master.configure(bg="white")  # Cambia el color de fondo a blanco

        # Imágenes
        self.imagen_agregar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\agregar.gif")
        self.imagen_escoba = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\escoba.gif")
        self.imagen_salir = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\cerrar-sesion.gif")

        # Labels
        self.cedula_label = tk.Label(master, background="white", text="Cédula:")
        self.nombre_label = tk.Label(master, background="white", text="Nombre:")
        self.apellidos_label = tk.Label(master, background="white", text="Apellidos:")
        self.telefono_label = tk.Label(master, background="white", text="Teléfono:")
        self.email_label = tk.Label(master, background="white", text="Email:")

        # Entrys
        self.cedula_entry = tk.Entry(master)
        self.nombre_entry = tk.Entry(master)
        self.apellidos_entry = tk.Entry(master)
        self.telefono_entry = tk.Entry(master)
        self.email_entry = tk.Entry(master)

        # Botones
        self.agregar_button = tk.Button(master, background="white", text="Agregar", image=self.imagen_agregar, command=self.agregar)
        self.limpiar_button = tk.Button(master, background="white", text="Limpiar", image=self.imagen_escoba, command=self.limpiar)
        self.salir_button = tk.Button(master, text="Salir", background="white", image=self.imagen_salir, command=self.salir)

        # Posicionamiento en la ventana
        self.cedula_label.place(x=60, y=20)
        self.cedula_entry.place(x=120, y=20)

        self.nombre_label.place(x=60, y=50)
        self.nombre_entry.place(x=120, y=50)

        self.apellidos_label.place(x=60, y=80)
        self.apellidos_entry.place(x=120, y=80)

        self.telefono_label.place(x=60, y=110)
        self.telefono_entry.place(x=120, y=110)

        self.email_label.place(x=60, y=140)
        self.email_entry.place(x=120, y=140)

        self.agregar_button.place(x=60, y=180, width=90)
        self.limpiar_button.place(x=170, y=180, width=90)
        self.salir_button.place(x=280, y=180, width=90)

        # Crear la tabla "Clientes" si no existe
        self.crear_tabla_clientes()

    def agregar(self):
        if self.verificar_condiciones():
            cedula = self.cedula_entry.get()
            nombre = self.nombre_entry.get()
            apellidos = self.apellidos_entry.get()
            telefono = self.telefono_entry.get()
            email = self.email_entry.get()

            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.insertar_registro_cliente(cedula, nombre, apellidos, telefono, email, fecha_hora_actual)

            mensaje = f"Cliente creado.\n\nDatos:\nCédula: {cedula}\nNombre: {nombre}\nApellidos: {apellidos}\nTeléfono: {telefono}\nEmail: {email}\n\nFecha y hora de registro: {fecha_hora_actual}"
            messagebox.showinfo("Registro Exitoso", mensaje)
            self.limpiar()

    def crear_tabla_clientes(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cedula VARCHAR(255),
                    nombre VARCHAR(255),
                    apellidos VARCHAR(255),
                    telefono VARCHAR(255),
                    email VARCHAR(255),
                    fecha_hora_registro DATETIME
                )
            """)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Error al crear la tabla 'Clientes':", error)

    def insertar_registro_cliente(self, cedula, nombre, apellidos, telefono, email, fecha_hora):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            query = "INSERT INTO Clientes (cedula, nombre, apellidos, telefono, email, fecha_hora_registro) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (cedula, nombre, apellidos, telefono, email, fecha_hora)
            cursor.execute(query, data)
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Error al insertar cliente:", error)

    def limpiar(self):
        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def salir(self):
        self.master.destroy()

    def verificar_condiciones(self):
        cedula = self.cedula_entry.get()
        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe contener solo números.")
            return False

        telefono = self.telefono_entry.get()
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe contener solo números.")
            return False

        nombre = self.nombre_entry.get()
        if not nombre.isalpha():
            messagebox.showerror("Error", "El nombre debe contener solo letras.")
            return False

        apellidos = self.apellidos_entry.get()
        if not apellidos.isalpha():
            messagebox.showerror("Error", "Los apellidos deben contener solo letras.")
            return False

        email = self.email_entry.get()
        if "@" not in email:
            messagebox.showerror("Error", "El email debe contener '@'.")
            return False

        return True







