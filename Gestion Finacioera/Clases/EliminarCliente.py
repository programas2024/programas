import tkinter as tk
from tkinter import messagebox
import mysql.connector

class EliminarCliente:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Clientes")
        self.master.geometry("400x300")
        self.master.configure(bg="white")  # Cambia el color de fondo a azul


        #imagenes

        self.imagen_elimanar = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\eliminar-usuario.gif")
        self.imagen_buscar=tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\buscar.gif")
        self.imagen_escoba = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\escoba.gif")
        self.imagen_salir = tk.PhotoImage(file="Gestion Finacioera\\Imagenes\\cerrar-sesion.gif")

        self.cedula_label = tk.Label(master,background="white", text="Cédula:")
        self.cedula_entry = tk.Entry(master)

        self.nombre_label = tk.Label(master,background="white", text="Nombre:")
        self.nombre_entry = tk.Entry(master, state=tk.DISABLED)  # Desactivar la caja de texto

        self.apellidos_label = tk.Label(master,background="white", text="Apellidos:")
        self.apellidos_entry = tk.Entry(master, state=tk.DISABLED)  # Desactivar la caja de texto

        self.telefono_label = tk.Label(master,background="white", text="Teléfono:")
        self.telefono_entry = tk.Entry(master, state=tk.DISABLED)  # Desactivar la caja de texto

        self.email_label = tk.Label(master,background="white", text="Email:")
        self.email_entry = tk.Entry(master, state=tk.DISABLED)  # Desactivar la caja de texto

        self.agregar_button = tk.Button(master, text="Agregar",background="white",image=self.imagen_elimanar, command=self.eliminar)
        self.limpiar_button = tk.Button(master, text="Limpiar",background="white",image=self.imagen_escoba ,command=self.limpiar)
        self.salir_button = tk.Button(master, text="Salir",background="white",image=self.imagen_salir ,command=self.salir)
        self.buscar_button = tk.Button(master, text="Buscar",background="white",image=self.imagen_buscar, command=self.buscar)

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
        self.buscar_button.place(x=280, y=50, width=90)  # Agregar el botón de búsqueda

    def eliminar(self):
        cedula = self.cedula_entry.get()

        if cedula:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                query = "DELETE FROM Clientes WHERE cedula = %s"
                cursor.execute(query, (cedula,))
                connection.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                    self.limpiar()
                else:
                    messagebox.showerror("Error", "Cliente no encontrado.")

                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al eliminar cliente:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese la cédula del cliente.")


    def limpiar(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def salir(self):
        self.master.destroy()

    def buscar(self):
        cedula = self.cedula_entry.get()

        if cedula:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                query = "SELECT * FROM Clientes WHERE cedula = %s"
                cursor.execute(query, (cedula,))
                cliente = cursor.fetchone()

                if cliente:
                    self.nombre_entry.config(state=tk.NORMAL)
                    self.apellidos_entry.config(state=tk.NORMAL)
                    self.telefono_entry.config(state=tk.NORMAL)
                    self.email_entry.config(state=tk.NORMAL)

                    self.nombre_entry.delete(0, tk.END)
                    self.nombre_entry.insert(0, cliente[2])  # Índice 1 para el nombre
                    self.apellidos_entry.delete(0, tk.END)
                    self.apellidos_entry.insert(0, cliente[3])  # Índice 2 para los apellidos
                    self.telefono_entry.delete(0, tk.END)
                    self.telefono_entry.insert(0, cliente[4])  # Índice 3 para el teléfono
                    self.email_entry.delete(0, tk.END)
                    self.email_entry.insert(0, cliente[5])  # Índice 4 para el email

                    self.nombre_entry.config(state=tk.DISABLED)
                    self.apellidos_entry.config(state=tk.DISABLED)
                    self.telefono_entry.config(state=tk.DISABLED)
                    self.email_entry.config(state=tk.DISABLED)
                else:
                    messagebox.showerror("Error", "Cliente no encontrado.")
                
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al buscar cliente:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese la cédula del cliente.")
