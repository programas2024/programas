import tkinter as tk
from RealizaraDeposito import RealizarDeposito
from RealizarRetiros import RealizarRetiro
class LaTransaccion:
    def __init__(self, master):
        self.master = master
        self.master.title("Transacción")
        self.master.geometry("300x300")
        self.master.configure(bg="white")

        self.label_titulo = tk.Label(master, text="Transacción", font=("Helvetica", 16), bg="white")
        self.label_titulo.place(x=100, y=10)

        self.btn_deposito = tk.Button(master, text="Depósito", command=self.realizar_deposito, bg="white")
        self.btn_deposito.place(x=100, y=50, width=100)

        self.btn_retiro = tk.Button(master, text="Retiro", command=self.realizar_retiro, bg="white")
        self.btn_retiro.place(x=100, y=90, width=100)

        self.btn_regresar = tk.Button(master, text="Regresar", command=self.regresar, bg="white")
        self.btn_regresar.place(x=100, y=130, width=100)

    def realizar_deposito(self):
        ventana_Corresponsal= tk.Toplevel(self.master)
        app_Corresponsal = RealizarDeposito(ventana_Corresponsal)

    def realizar_retiro(self):
        ventana_Corresponsal= tk.Toplevel(self.master)
        app_Corresponsal = RealizarRetiro(ventana_Corresponsal)

    def regresar(self):
        self.master.destroy()

