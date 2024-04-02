import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

class MostrarClientes:
    def __init__(self, master):
        self.master = master
        self.master.title("Mostrar Clientes")
        self.master.geometry("1500x600")  # Maximizar la ventana al ser llamada

        self.frame = tk.Frame(master, bg="white", bd=2, relief="solid")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=1400, height=500)

        self.btn_consultar = tk.Button(master, text="Consultar", command=self.consultar)
        self.btn_consultar.place(x=200, y=550)

        self.btn_cancelar = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.btn_cancelar.place(x=300, y=550)

        self.btn_modo = tk.Button(master, text="Modo", command=self.cambiar_modo)
        self.btn_modo.place(x=400, y=550)

        self.modo_texto = True  # Flag para rastrear el modo de visualización actual
        self.treeview = None  # Variable para almacenar el widget Treeview

    def consultar(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                database="financiera"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Clientes")
            clientes = cursor.fetchall()

            if self.modo_texto:
                self.mostrar_clientes_texto(clientes)
            else:
                self.mostrar_clientes_tabla(clientes)

            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al consultar clientes: {error}")

    def mostrar_clientes_texto(self, clientes):
        if self.treeview:
            self.treeview.destroy()

        for widget in self.frame.winfo_children():
            widget.destroy()

        y = 20
        for cliente in clientes:
            texto_cliente = f"ID: {cliente[0]}, Cédula: {cliente[1]}, Nombre: {cliente[2]}, Apellidos: {cliente[3]}, Teléfonos: {cliente[4]}, Email: {cliente[5]}, Fecha y Hora de Registro: {cliente[6]}"
            tk.Label(self.frame, text=texto_cliente, anchor="center", bg="white").place(relx=0.5, y=y, anchor="center")
            y += 20

    def mostrar_clientes_tabla(self, clientes):
        if self.treeview:
            self.treeview.destroy()

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.treeview = ttk.Treeview(self.frame, columns=("ID", "Cédula", "Nombre", "Apellidos", "Teléfono", "Email", "Fecha y Hora de Registro"))
        self.treeview.place(relx=0.5, y=10, anchor="n")

        self.treeview.heading("#0", text="No.")
        self.treeview.column("#0", width=30)
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Cédula", text="Cédula")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellidos", text="Apellidos")
        self.treeview.heading("Teléfono", text="Teléfono")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Fecha y Hora de Registro", text="Fecha y Hora de Registro")

        for i, cliente in enumerate(clientes, start=1):
            self.treeview.insert("", "end", text=str(i), values=cliente)

    def cancelar(self):
        self.master.destroy()

    def cambiar_modo(self):
        self.modo_texto = not self.modo_texto
        self.consultar()





