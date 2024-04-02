import tkinter as tk
import mysql.connector
from tkinter import messagebox

class Generar:
    def __init__(self, master):
        self.master = master
        self.master.title("Generar")
        self.master.geometry("1500x600")
        self.master.config(bg="white")

        # Crear lienzo centrado con marco negro
        self.lienzo = tk.Canvas(master, bg="white", width=1000, height=400, highlightbackground="black", highlightthickness=1)
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center")

        # Crear label "Generar"
        self.label_generar = tk.Label(self.lienzo, text="Generar", font=("Helvetica", 24), bg="white")
        self.label_generar.place(relx=0.5, rely=0.1, anchor="center")

        # Crear etiqueta para mostrar información de cuentas
        self.label_cuentas = tk.Label(self.lienzo, text="", font=("Helvetica", 12), bg="white")
        self.label_cuentas.place(relx=0.5, rely=0.3, anchor="center")

        # Crear etiqueta para mostrar información de retiros
        self.label_retiros = tk.Label(self.lienzo, text="", font=("Helvetica", 12), bg="white")
        self.label_retiros.place(relx=0.8, rely=0.2, anchor="center")

        # Crear etiqueta para mostrar información de depósitos
        self.label_depositos = tk.Label(self.lienzo, text="", font=("Helvetica", 12), bg="white")
        self.label_depositos.place(relx=0.8, rely=0.4, anchor="center")

        # Crear botón "Consultar"
        self.btn_consultar = tk.Button(self.lienzo, text="Consultar", font=("Helvetica", 14), command=self.consultar, bg="#4CAF50", fg="white")
        self.btn_consultar.place(relx=0.3, rely=0.7, anchor="center")

        # Crear botón "Cancelar"
        self.btn_cancelar = tk.Button(self.lienzo, text="Cancelar", font=("Helvetica", 14), command=self.cancelar, bg="#FF5733", fg="white")
        self.btn_cancelar.place(relx=0.7, rely=0.7, anchor="center")

    def consultar(self):
        try:
            connection = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                user="root",
                port="30449",
                password="RpIrXdsVKDEZCasxXTmPsJkNFdILQYRo",
                database="financiera"
            )
            cursor = connection.cursor()

            # Consultar la tabla "Cuenta"
            cursor.execute("SELECT * FROM Cuenta")
            cuentas = cursor.fetchall()
            cuentas_info = "Cuentas:\n"
            for cuenta in cuentas:
                cuentas_info += f"Número de cuenta: {cuenta[1]}, Saldo: {cuenta[2]}\n, cedula_cliente: {cuenta[3]}\n, fecha_hora_creacion: {cuenta[4]}\n"

            # Consultar la tabla "Retiros"
            cursor.execute("SELECT * FROM Retiros")
            retiros = cursor.fetchall()
            retiros_info = "Retiros:\n"
            for retiro in retiros:
                retiros_info += f"Monto: {retiro[2]}\n"

            # Consultar la tabla "Depositos"
            cursor.execute("SELECT * FROM Deposito")
            depositos = cursor.fetchall()
            depositos_info = "Depósitos:\n"
            for deposito in depositos:
                depositos_info += f"Monto: {deposito[2]}\n"

            # Mostrar la información en las etiquetas
            self.label_cuentas.config(text=cuentas_info)
            self.label_retiros.config(text=retiros_info)
            self.label_depositos.config(text=depositos_info)

            cursor.close()
            connection.close()
            messagebox.showinfo("Consulta exitosa", "Consulta realizada correctamente.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al consultar la base de datos: {error}")

    def cancelar(self):
        self.master.destroy()






