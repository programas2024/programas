from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import mysql.connector


class EliminarCuenta:
    def __init__(self, master):
        self.master = master
        self.master.title("Eliminar Cuenta")
        self.master.geometry("400x200")
        self.master.configure(bg="white")  

        self.label_titulo = tk.Label(master, text="Eliminar Cuenta", font=("Helvetica", 16), bg="white")
        self.label_titulo.place(x=150, y=10)

        self.label_numero_cuenta = tk.Label(master, text="Número de Cuenta:", bg="white")
        self.label_numero_cuenta.place(x=30, y=50)
        
      
        self.entry_numero_cuenta = tk.Entry(master)
        self.entry_numero_cuenta.place(x=160, y=50)

        self.label_saldo = tk.Label(master, text="Saldo:", bg="white")
        self.label_saldo.place(x=30, y=80)
        self.entry_saldo = tk.Entry(master, state=tk.DISABLED)
        self.entry_saldo.place(x=160, y=80)

        self.label_cedula = tk.Label(master, text="Cédula:", bg="white")
        self.label_cedula.place(x=30, y=110)
        self.entry_cedula = tk.Entry(master, state=tk.DISABLED)
        self.entry_cedula.place(x=160, y=110)

        self.btn_buscar = tk.Button(master, text="Buscar", command=self.buscar)
        self.btn_buscar.place(x=60, y=150)

        
        self.btn_eliminar = tk.Button(master, text="Eliminar Cuenta", command=self.eliminar_cuenta, state=tk.DISABLED)
        self.btn_eliminar.place(x=220, y=150)

        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.place(x=290, y=150)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.place(x=360, y=150)

    
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
                    self.entry_saldo.config(state=tk.NORMAL)
                    self.entry_cedula.config(state=tk.NORMAL)
                    self.btn_buscar.config(state=tk.NORMAL)
                    self.btn_eliminar.config(state=tk.NORMAL)

                    self.entry_saldo.delete(0, tk.END)
                    self.entry_saldo.insert(0, cuenta[2])  # Índice 1 para el saldo
                    self.entry_cedula.delete(0, tk.END)
                    self.entry_cedula.insert(0, cuenta[3])  # Índice 2 para la cédula

                    self.entry_saldo.config(state=tk.DISABLED)
                    self.entry_cedula.config(state=tk.DISABLED)

                    messagebox.showinfo("Éxito", "Cuenta encontrada.")
                else:
                    messagebox.showerror("Error", "Cuenta no encontrada.")
                
                cursor.close()
                connection.close()
            except mysql.connector.Error as error:
                print("Error al buscar cuenta:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese el número de cuenta.")

    def eliminar_cuenta(self):
        numero_cuenta = self.entry_numero_cuenta.get()

        if numero_cuenta:
            try:
                connection = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    database="financiera"
                )
                cursor = connection.cursor()

                query = "DELETE FROM Cuenta WHERE numero_cuenta = %s"
                cursor.execute(query, (numero_cuenta,))
                connection.commit()

                messagebox.showinfo("Éxito", "Cuenta eliminada correctamente.")
                
                cursor.close()
                connection.close()

                # Limpiar los campos después de eliminar la cuenta
                self.limpiar()
            except mysql.connector.Error as error:
                print("Error al eliminar cuenta:", error)
        else:
            messagebox.showerror("Error", "Por favor ingrese el número de cuenta.")
    def limpiar(self):
        self.entry_numero_cuenta.delete(0, tk.END)
        self.entry_saldo.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        self.btn_buscar.config(state=tk.NORMAL)
        self.btn_eliminar.config(state=tk.DISABLED)

    def cancelar(self):
        self.master.destroy()

