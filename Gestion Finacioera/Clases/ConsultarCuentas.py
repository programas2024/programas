import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class ConsultarCuentas:
    def __init__(self, master):
        self.master = master
        self.master.title("Consultar Cuentas")
        self.master.geometry("1500x600")

        self.canvas = tk.Canvas(master, bg="white", width=1000, height=300)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.label_cuentas = tk.Label(self.canvas, text="Total de cuentas", bg="white", justify="left")
        self.label_cuentas.place(x=20, y=20)

        self.label_total_cuentas = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_total_cuentas.place(x=600, y=20)

        self.label_mayor_millon = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_mayor_millon.place(x=600, y=70)

        self.label_menor_millon = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_menor_millon.place(x=600, y=100)

        self.label_tiempo = tk.Label(self.canvas, text="", bg="white", justify="left")
        self.label_tiempo.place(x=20, y=150)

        self.btn_consultar = tk.Button(master, text="Consultar", command=self.consultar_cuentas)
        self.btn_consultar.place(x=50, anchor="center", y=350)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.place(x=50, anchor="center", y=400)

        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.numero_cuenta = None

        # Crear tabla "ConsultasCuentas" si no existe
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
                CREATE TABLE IF NOT EXISTS ConsultasCuentas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    numero_cuenta VARCHAR(255),
                    tiempo_transcurrido INT
                )
            """)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al crear tabla ConsultasCuentas: {error}")

    def consultar_cuentas(self):
        self.tiempo_inicio = datetime.now()

        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT numero_cuenta, saldo, cedula_cliente FROM Cuenta")
            cuentas = cursor.fetchall()

            # Mostrar información de las cuentas
            self.mostrar_cuentas(cuentas)

            # Actualizar el tiempo transcurrido en la interfaz
            self.actualizar_tiempo()

            # Guardar el número de cuenta para utilizarlo posteriormente
            self.numero_cuenta = cuentas[0][0] if cuentas else None

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al consultar cuentas: {error}")

    def mostrar_cuentas(self, cuentas):
        if cuentas:
            texto_cuentas = "\n".join([f"Número de Cuenta: {cuenta[0][:4]}****\nSaldo: {cuenta[1]}\nCédula: {cuenta[2]}" for cuenta in cuentas])
            self.label_cuentas.config(text=texto_cuentas)
            self.label_total_cuentas.config(text=f"Total de cuentas: {len(cuentas)}")

            # Calcular cantidad de cuentas con saldo mayor y menor a un millón
            cuentas_mayor_millon = sum(1 for cuenta in cuentas if cuenta[1] > 1000000)
            cuentas_menor_millon = len(cuentas) - cuentas_mayor_millon
            self.label_mayor_millon.config(text=f"Cuentas con saldo mayor a 1 millón: {cuentas_mayor_millon}")
            self.label_menor_millon.config(text=f"Cuentas con saldo menor a 1 millón: {cuentas_menor_millon}")

        else:
            self.label_cuentas.config(text="No hay cuentas registradas")
            self.label_total_cuentas.config(text="Total de cuentas: 0")
            self.label_mayor_millon.config(text="Cuentas con saldo mayor a 1 millón: 0")
            self.label_menor_millon.config(text="Cuentas con saldo menor a 1 millón: 0")

    def actualizar_tiempo(self):
        tiempo_actual = datetime.now()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
        tiempo_formato = f"Tiempo transcurrido: {int(tiempo_transcurrido.total_seconds())} segundos"
        self.label_tiempo.config(text=tiempo_formato)
        self.master.after(1000, self.actualizar_tiempo)

    def guardar_tiempo_consulta(self):
        try:
            if self.tiempo_inicio and self.tiempo_fin and self.numero_cuenta:
                tiempo_transcurrido = (self.tiempo_fin - self.tiempo_inicio).total_seconds()

                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                cursor.execute("INSERT INTO ConsultasCuentas (numero_cuenta, tiempo_transcurrido) VALUES (%s, %s)", (self.numero_cuenta, int(tiempo_transcurrido)))
                
                connection.commit()

                cursor.close()
                connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al guardar tiempo de consulta: {error}")

    def cancelar(self):
        self.tiempo_fin = datetime.now()
        self.guardar_tiempo_consulta()
        self.master.destroy()


















