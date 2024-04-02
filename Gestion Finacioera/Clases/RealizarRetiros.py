import tkinter as tk
from tkinter import messagebox
import mysql.connector
import random
from datetime import datetime

class RealizarRetiro:
    def __init__(self, master):
        self.master = master
        self.master.title("Realizar Retiro")
        self.master.geometry("400x200")
        self.master.configure(bg="white")

        self.label_titulo = tk.Label(master, text="Realizar Retiro", font=("Helvetica", 16), bg="white")
        self.label_titulo.place(x=120, y=10)

        self.label_numero_cuenta = tk.Label(master, text="Número de Cuenta:", bg="white")
        self.label_numero_cuenta.place(x=30, y=50)
        self.entry_numero_cuenta = tk.Entry(master)
        self.entry_numero_cuenta.place(x=160, y=50)

        self.label_monto = tk.Label(master, text="Monto:", bg="white")
        self.label_monto.place(x=30, y=80)
        self.entry_monto = tk.Entry(master, state=tk.DISABLED)
        self.entry_monto.place(x=160, y=80)

        self.label_numero_transaccion = tk.Label(master, text="Número de Transacción:", bg="white" )
        self.label_numero_transaccion.place(x=30, y=110)
        self.entry_numero_transaccion = tk.Entry(master)
        self.entry_numero_transaccion.place(x=160, y=110)

        self.btn_buscar = tk.Button(master, text="Buscar", command=self.buscar, bg="white")
        self.btn_buscar.place(x=60, y=150)

        self.btn_retiro = tk.Button(master, text="Realizar Retiro", command=self.realizar_retiro, bg="white", state=tk.DISABLED)
        self.btn_retiro.place(x=120, y=150)

        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar, bg="white")
        self.btn_limpiar.place(x=250, y=150)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar, bg="white")
        self.btn_cancelar.place(x=320, y=150)

        # Verificar y crear la tabla Retiros si no existe
        self.verificar_tabla_retiros()

    def verificar_tabla_retiros(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS Retiros (id INT AUTO_INCREMENT PRIMARY KEY, numero_cuenta VARCHAR(255), monto DECIMAL(10, 2), numero_transaccion VARCHAR(255), fecha_hora DATETIME)")

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print("Error al verificar la tabla Retiros:", error)

    def buscar(self):
        numero_cuenta = self.entry_numero_cuenta.get()

        if numero_cuenta:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                query = "SELECT * FROM Cuenta WHERE numero_cuenta = %s"
                cursor.execute(query, (numero_cuenta,))
                cuenta = cursor.fetchone()

                if cuenta:
                    self.entry_monto.config(state=tk.NORMAL)
                    self.btn_retiro.config(state=tk.NORMAL)
                    self.entry_monto.focus_set()  # Enfocar la caja de monto
                    self.entry_numero_transaccion.insert(0, self.generar_numero_transaccion())
                    messagebox.showinfo("Éxito", "Cuenta encontrada. Puede realizar el retiro.")
                else:
                    self.entry_monto.config(state=tk.DISABLED)
                    self.btn_retiro.config(state=tk.DISABLED)
                    messagebox.showerror("Error", "Cuenta no encontrada.")
                
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al buscar cuenta:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese el número de cuenta.")

    def generar_numero_transaccion(self):
        return str(random.randint(100000, 999999))

    def realizar_retiro(self):
        numero_cuenta = self.entry_numero_cuenta.get()
        monto = float(self.entry_monto.get())
        numero_transaccion = self.entry_numero_transaccion.get()
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            # Verificar si hay saldo suficiente
            cursor.execute("SELECT saldo FROM Cuenta WHERE numero_cuenta = %s", (numero_cuenta,))
            saldo_actual = cursor.fetchone()[0]

            if saldo_actual < monto:
                messagebox.showerror("Error", "Saldo insuficiente para realizar el retiro.")
                return

            # Actualizar el saldo de la cuenta
            cursor.execute("UPDATE Cuenta SET saldo = saldo - %s WHERE numero_cuenta = %s", (monto, numero_cuenta))

            # Insertar los datos del retiro
            query = "INSERT INTO Retiros (numero_cuenta, monto, numero_transaccion, fecha_hora) VALUES (%s, %s, %s, %s)"
            data = (numero_cuenta, monto, numero_transaccion, fecha_hora)
            cursor.execute(query, data)

            connection.commit()

            messagebox.showinfo("Éxito", "Retiro realizado correctamente.")
            
            cursor.close()
            connection.close()

            # Limpiar las cajas y generar un nuevo número de transacción
            self.limpiar()
            self.entry_numero_transaccion.insert(0, self.generar_numero_transaccion())
        except mysql.connector.Error as error:
            print("Error al realizar retiro:", error)

    def limpiar(self):
        self.entry_numero_cuenta.delete(0, tk.END)
        self.entry_monto.delete(0, tk.END)
        self.entry_numero_transaccion.delete(0, tk.END)
        self.entry_monto.config(state=tk.DISABLED)
        self.btn_retiro.config(state=tk.DISABLED)

    def cancelar(self):
        self.master.destroy()


