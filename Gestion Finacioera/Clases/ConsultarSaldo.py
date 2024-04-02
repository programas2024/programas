import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime, timedelta

class ConsultarSaldo:
    def __init__(self, master):
        self.master = master
        self.master.title("Consultar Saldo")
        self.master.geometry("1500x600")

        self.canvas = tk.Canvas(master, bg="white", width=1000, height=300)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.label_saldos = tk.Label(self.canvas, text="Saldos de cuentas", bg="white", justify="left")
        self.label_saldos.place(x=20, y=20)

        self.label_total_saldos = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_total_saldos.place(x=500, y=20)

        self.label_tiempo = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_tiempo.place(x=500, y=70)

        self.btn_consultar = tk.Button(master, text="Consultar", command=self.consultar_saldos)
        self.btn_consultar.place(x=50, anchor="center", y=350)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.place(x=50, anchor="center", y=400)

        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.saldos = None

        # Crear tabla "ConsultasSaldo" si no existe
        self.crear_tabla_consultas()

    def crear_tabla_consultas(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Saldos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    numero_cuenta VARCHAR(255),
                    cedula_cliente VARCHAR(255),
                    saldo DECIMAL(10, 2),
                    tiempo_transcurrido INT
                )
            """)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al crear tabla ConsultasSaldos: {error}")

    def consultar_saldos(self):
        self.tiempo_inicio = datetime.now()

        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT cedula_cliente, saldo, numero_cuenta FROM Cuenta")
            self.saldos = cursor.fetchall()

            # Mostrar información de los saldos
            self.mostrar_saldos(self.saldos)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al consultar saldos: {error}")

    def mostrar_saldos(self, saldos):
        if saldos:
            texto_saldos = "\n".join([f"Número de Cuenta: {saldo[2]}\nCédula: {saldo[0][:len(saldo[0])-4]}****\nSaldo: {saldo[1]}" for saldo in saldos])
            self.label_saldos.config(text=texto_saldos)
            self.label_total_saldos.config(text=f"Total de cuentas: {len(saldos)}")

            # Actualizar el tiempo transcurrido en la interfaz
            self.actualizar_tiempo()
        else:
            self.label_saldos.config(text="No hay saldos registrados")
            self.label_total_saldos.config(text="Total de cuentas: 0")

    def actualizar_tiempo(self):
        self.tiempo_fin = datetime.now()
        tiempo_transcurrido = self.tiempo_fin - self.tiempo_inicio
        tiempo_formato = f"Tiempo transcurrido: {int(tiempo_transcurrido.total_seconds())} segundos"
        self.label_tiempo.config(text=tiempo_formato)
        self.master.after(1000, self.actualizar_tiempo)

    def guardar_tiempo_consulta(self):
        try:
            if self.tiempo_inicio and self.tiempo_fin and self.saldos:
                tiempo_transcurrido = (self.tiempo_fin - self.tiempo_inicio).total_seconds()

                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                for saldo in self.saldos:
                    cursor.execute("INSERT INTO Saldos (numero_cuenta, cedula_cliente, saldo, tiempo_transcurrido) VALUES (%s, %s, %s, %s)", (saldo[2], saldo[0], saldo[1], int(tiempo_transcurrido)))
                
                connection.commit()

                cursor.close()
                connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al guardar tiempo de consulta: {error}")

    def cancelar(self):
        self.guardar_tiempo_consulta()  # Guardar tiempo al cerrar la interfaz
        self.master.destroy()



