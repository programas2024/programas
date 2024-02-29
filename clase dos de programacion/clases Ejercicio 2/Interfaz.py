from CalcularPotencia import CalcularPontencia
import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Potencia")
        self.master.geometry("400x250")  # Tamaño de la ventana

        self.potencia_calculadora = CalcularPontencia()

        self.label_base = tk.Label(master, text="Número Base:")
        self.label_base.place(x=10, y=40)
        self.caja_base = tk.Entry(master)
        self.caja_base.place(x=150, y=40)

        self.label_exponente = tk.Label(master, text="Exponente:")
        self.label_exponente.place(x=10, y=70)
        self.opciones_exponente = [str(i) for i in range(1, 11)]  # Opciones de 1 a 10
        self.caja_exponente = tk.StringVar(master)
        self.caja_exponente.set(self.opciones_exponente[0])  # Establece el valor predeterminado
        self.menu_exponente = tk.OptionMenu(master, self.caja_exponente, *self.opciones_exponente)
        self.menu_exponente.place(x=150, y=70)

        self.label_resultado = tk.Label(master, text="Resultado:")
        self.label_resultado.place(x=10, y=100)
        self.caja_resultado = tk.Entry(master, state='readonly', readonlybackground='white')
        self.caja_resultado.place(x=150, y=100)

        self.boton_consultar = tk.Button(master, text="Consultar", command=self.consultar)
        self.boton_salir = tk.Button(master, text="Salir", command=self.salir)

        self.boton_consultar.place(x=150, y=130)
        self.boton_salir.place(x=150, y=160)

    def consultar(self):
        try:
            base = float(self.caja_base.get())
            exponente = int(self.caja_exponente.get())

            resultado = self.potencia_calculadora.calcular_potencia(base, exponente)

            messagebox.showinfo("Resultado", f"{base}^{exponente} es igual a {resultado}")

            self.caja_resultado.config(state='normal')
            self.caja_resultado.delete(0, tk.END)
            self.caja_resultado.insert(0, str(resultado))
            self.caja_resultado.config(state='readonly')

        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido para la base")

    def salir(self):
        self.master.destroy()