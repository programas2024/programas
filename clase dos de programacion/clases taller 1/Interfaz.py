import tkinter as tk
from tkinter import messagebox
from Acumulativa import Acumulativa
from Evento import Evento
from Limpiar import Limpiar
class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Acumulativa")
        self.master.geometry("400x250")  # Ajusté el tamaño de la ventana
        self.master.configure(bg="white")

        self.primer_consulta = True 

        self.calculadora = Acumulativa()

        self.label_titulo = tk.Label(master, text="Número Reales")
        self.label_titulo.place(x=200, y=10, anchor="center")

        self.label_numero1 = tk.Label(master, text="Número 1")
        self.label_numero1.place(x=10, y=40)
        self.caja1 = tk.Entry(master)
        self.caja1.place(x=150, y=40)
        self.caja1.focus_set()  # Coloca el foco en la primera caja al iniciar la aplicación
        self.configurar_evento(self.caja1)

        self.label_numero2 = tk.Label(master, text="Número 2")
        self.label_numero2.place(x=10, y=70)
        self.caja2 = tk.Entry(master, state='readonly')
        self.caja2.place(x=150, y=70)
        self.configurar_evento(self.caja2)

        self.label_numero3 = tk.Label(master, text="Número 3")
        self.label_numero3.place(x=10, y=100)
        self.caja3 = tk.Entry(master, state='readonly')
        self.caja3.place(x=150, y=100)
        self.configurar_evento(self.caja3)

        self.label_resultado = tk.Label(master, text="Resultado")
        self.label_resultado.place(x=10, y=130)
        self.caja_resultado = tk.Entry(master, state='readonly', readonlybackground='white')
        self.caja_resultado.place(x=150, y=130)

        self.boton_consultar = tk.Button(master, text="Consultar", command=self.consultar)
        self.boton_salir = tk.Button(master, text="Salir", command=self.salir)

        self.boton_consultar.place(x=150, y=160)
        self.boton_salir.place(x=150, y=190)

    def configurar_evento(self, caja):
        evento = Evento(caja, self)

    def consultar(self):
        try:
            num1 = float(self.caja1.get().replace(",", ""))
            num2 = float(self.caja2.get().replace(",", ""))
            num3 = float(self.caja3.get().replace(",", ""))

            if self.primer_consulta:
                self.calculadora.agregar_numero(num1)
                self.calculadora.agregar_numero(num2)
                self.calculadora.agregar_numero(num3)
                self.primer_consulta = False  # Después de la primera consulta, ya no es la primera

            else:
                self.calculadora = Acumulativa()  # Reinicia la calculadora
                self.calculadora.agregar_numero(num1)
                self.calculadora.agregar_numero(num2)
                self.calculadora.agregar_numero(num3)

            resultado = self.calculadora.obtener_resultado()
            resultado_str = str(int(resultado)) if resultado.is_integer() else str(resultado)

            messagebox.showinfo("Resultado", f"El valor acumulado es: {resultado_str}")

            limpiar_cajas = Limpiar([self.caja1, self.caja2, self.caja3, self.caja_resultado])
            limpiar_cajas.limpiar()

            # Cambia el enfoque a la primera caja
            self.caja1.config(state='normal')
            self.caja1.focus_set()  # Coloca el foco en la primera caja

            self.caja_resultado.config(state='readonly')

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")


    def cambiar_caja(self, caja_actual, caja_siguiente):
        caja_actual.config(state='readonly')
        caja_siguiente.config(state='normal')
        caja_siguiente.delete(0, tk.END)
        caja_siguiente.focus_set()  # Coloca el foco en la siguiente caja

    def salir(self):
        self.master.destroy()