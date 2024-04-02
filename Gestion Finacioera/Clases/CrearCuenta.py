from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random

class CrearCuenta:
    def __init__(self, master):
        self.master = master
        self.master.title("Crear Cuenta")
        self.master.geometry("400x200")
        self.master.configure(bg="white")  

        self.label_titulo = tk.Label(master, text="Crear Cuenta", font=("Helvetica", 16), bg="white")
        self.label_titulo.place(x=150, y=10)

        self.label_numero_cuenta = tk.Label(master, text="Número de Cuenta:", bg="white")
        self.label_numero_cuenta.place(x=30, y=50)
        self.numero_cuenta = tk.StringVar()
        self.numero_cuenta.set(self.generar_numero_cuenta())
        self.entry_numero_cuenta = tk.Entry(master, textvariable=self.numero_cuenta, state='readonly')
        self.entry_numero_cuenta.place(x=160, y=50)

        self.label_saldo = tk.Label(master, text="Saldo:", bg="white")
        self.label_saldo.place(x=30, y=80)
        self.entry_saldo = tk.Entry(master)
        self.entry_saldo.place(x=160, y=80)

        self.label_cedula = tk.Label(master, text="Cédula:", bg="white")
        self.label_cedula.place(x=30, y=110)
        self.entry_cedula = tk.Entry(master)
        self.entry_cedula.place(x=160, y=110)

        self.btn_buscar = tk.Button(master, text="Buscar", command=self.buscar)
        self.btn_buscar.place(x=60, y=150)

        self.btn_crear = tk.Button(master, text="Crear Cuenta", command=self.crear_cuenta, state=tk.DISABLED)
        self.btn_crear.place(x=120, y=150)

        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=220, y=150)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.place(x=290, y=150)

    def generar_numero_cuenta(self):
        return str(random.randint(1000000000, 9999999999))

    def buscar(self):
        cedula = self.entry_cedula.get()

        if cedula:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                # Verificar si la tabla 'Cuenta' existe, y crearla si no existe
                cursor.execute("SHOW TABLES LIKE 'Cuenta'")
                result = cursor.fetchone()
                if not result:
                    # La tabla 'Cuenta' no existe, entonces la creamos
                    cursor.execute("""
                        CREATE TABLE Cuenta (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            numero_cuenta VARCHAR(255),
                            saldo DECIMAL(10, 2),
                            cedula_cliente VARCHAR(255),
                            fecha_hora_creacion DATETIME,
                            momento_creacion VARCHAR(50)
                        )
                    """)

                query = "SELECT * FROM Cuenta WHERE cedula_cliente = %s"
                cursor.execute(query, (cedula,))
                cuenta = cursor.fetchone()

                if cuenta:
                    self.btn_crear.config(state=tk.DISABLED)
                    messagebox.showinfo("Información", "Este cliente ya tiene una cuenta asociada.")
                else:
                    self.btn_crear.config(state=tk.NORMAL)
                    messagebox.showinfo("Información", "Cliente válido para crear cuenta.")
                
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al buscar cuenta:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese la cédula del cliente.")


    def crear_cuenta(self):
        numero_cuenta = self.entry_numero_cuenta.get()
        saldo = self.entry_saldo.get()
        cedula = self.entry_cedula.get()

        if cedula:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                now = datetime.now()
                fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
                hora = now.strftime("%H")

                if 6 <= int(hora) < 18:
                    momento = "de día"
                else:
                    momento = "de noche"

                query = "INSERT INTO Cuenta (numero_cuenta, saldo, cedula_cliente, fecha_hora_creacion, momento_creacion) VALUES (%s, %s, %s, %s, %s)"
                data = (numero_cuenta, saldo, cedula, fecha_hora, momento)
                cursor.execute(query, data)
                connection.commit()

                messagebox.showinfo("Éxito", "Cuenta creada correctamente.")

                # Actualizar el número de cuenta
                self.numero_cuenta.set(self.generar_numero_cuenta())
                
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al crear cuenta:", error)
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def limpiar(self):
        self.entry_saldo.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        self.btn_crear.config(state=tk.DISABLED)

    def cancelar(self):
        self.master.destroy()

