import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import PhotoImage


class Interfaz:
    def __init__(self, master, logica):
        self.master = master
        self.master.title("Calculadora de Descuento")
        self.master.geometry("550x400")  # Tamaño de la ventana
        self.master.config(bg="white")

        self.tv=tk.PhotoImage(file="Imagenes\\television-inteligente.png")
        self.pos=tk.PhotoImage(file="Imagenes\\pos.png")
        self.cinta=tk.PhotoImage(file="Imagenes\\cinta.png")

        self.equipo_sonido = tk.PhotoImage(file="Imagenes\\altavoz.png")
        self.nevera = tk.PhotoImage(file="Imagenes\\nevera.png")
        self.computador = tk.PhotoImage(file="Imagenes\\ordenador.png")



        self.logica_producto = logica

        self.label_valor_original = tk.Label(master, text="LISTA DE PRODUCTOS",background="white")
        self.label_valor_original.place(x=30, y=20)

        self.label_nombre = tk.Label(master, text="Nombre del Producto:",background="white")
        self.label_nombre.place(x=230, y=40)
        self.caja_nombre = tk.Entry(master,borderwidth=2)
        self.caja_nombre.place(x=370, y=40)

        self.label_valor_original = tk.Label(master, text="Valor Original:",background="white")
        self.label_valor_original.place(x=230, y=70)
        self.caja_valor_original = tk.Entry(master,borderwidth=2)
        self.caja_valor_original.place(x=370, y=70)

        self.boton_televisor = tk.Button(master, text="", command=self.mostrar_televisor,image=self.tv,borderwidth=0,bg="white")
        self.boton_televisor.place(x=10, y=100)

        self.label_descuento = tk.Label(master, text="Descuento (%):",background="white")
        self.label_descuento.place(x=230, y=100)
        self.caja_descuento = tk.Entry(master,borderwidth=2)
        self.caja_descuento.place(x=370, y=100)

        self.label_valor_final = tk.Label(master, text="Valor a Pagar:",background="white")
        self.label_valor_final.place(x=230, y=130)
        self.caja_valor_final = tk.Entry(master,borderwidth=2)
        self.caja_valor_final.place(x=370, y=130)

        self.boton_oferta = tk.Button(master, text="Oferta", command=self.aplicar_oferta,image=self.cinta,bg="white")
        self.boton_oferta.place(x=230, y=190)

        self.boton_pagar = tk.Button(master, text="", command=self.mostrar_pago,image=self.pos,bg="white")
        self.boton_pagar.place(x=330, y=190)

        self.boton_sonido = tk.Button(master, text="", command=self.mostrar_equipo_sonido, image=self.equipo_sonido, borderwidth=0, bg="white")
        self.boton_sonido.place(x=110, y=100)

        self.boton_nevera = tk.Button(master, text="", command=self.mostrar_nevera, image=self.nevera, borderwidth=0, bg="white")
        self.boton_nevera.place(x=10, y=180)

        self.boton_computador = tk.Button(master, text="", command=self.mostrar_computador, image=self.computador, borderwidth=0, bg="white")
        self.boton_computador.place(x=100, y=180)


    def mostrar_televisor(self):
        self.logica_producto.nombre_producto = "Televisor"
        self.logica_producto.valor_original = 950000
        self.actualizar_resultado()

    def mostrar_equipo_sonido(self):
        self.logica_producto.nombre_producto = "Equipo de Sonido"
        self.logica_producto.valor_original = 20000
        self.actualizar_resultado()

    def mostrar_nevera(self):
        self.logica_producto.nombre_producto = "Nevera"
        self.logica_producto.valor_original = 200000
        self.actualizar_resultado()

    def mostrar_computador(self):
        self.logica_producto.nombre_producto = "Computador"
        self.logica_producto.valor_original = 1500000
        self.actualizar_resultado()

    def aplicar_oferta(self):
        self.logica_producto.descuento_porcentaje = 19
        self.actualizar_resultado()

    def actualizar_resultado(self):
        self.caja_nombre.delete(0, tk.END)
        self.caja_nombre.insert(0, self.logica_producto.nombre_producto)

        self.caja_valor_original.delete(0, tk.END)
        self.caja_valor_original.insert(0, str(self.logica_producto.valor_original))

        self.caja_descuento.delete(0, tk.END)
        self.caja_descuento.insert(0, str(self.logica_producto.descuento_porcentaje))

        _, valor_a_pagar = self.logica_producto.aplicar_descuento()
        self.caja_valor_final.delete(0, tk.END)
        self.caja_valor_final.insert(0, str(valor_a_pagar))

    def mostrar_pago(self):
        descuento, valor_a_pagar = self.logica_producto.aplicar_descuento()
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje_pago = f"Fecha y Hora: {fecha_hora_actual}\n"
        mensaje_pago += f"Producto: {self.logica_producto.nombre_producto}\n"
        mensaje_pago += f"Valor Original: ${self.logica_producto.valor_original:,.2f}\n"
        mensaje_pago += f"Descuento ({self.logica_producto.descuento_porcentaje}%): ${descuento:,.2f}\n"
        mensaje_pago += f"Valor a Pagar: ${valor_a_pagar:,.2f}"
        messagebox.showinfo("Detalle del Pago", mensaje_pago)