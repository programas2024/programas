import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk 

class CorresponsalInvitado:
    def __init__(self, root):
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        root.geometry("900x500")
        root.configure(bg="white")


        image_path = 'Imagenes\\bitcoin-con-la-mano.png'
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Crear un widget Label para mostrar la imagen
        self.label_image = tk.Label(root,bg="white", image=self.photo)
        self.label_image.place(x=4,y=50)


        image_path6 = 'Imagenes\\control-de-versiones.png'
        self.image6 = Image.open(image_path6)
        self.photo6 = ImageTk.PhotoImage(self.image6)

        # Crear un widget Label para mostrar la imagen
        self.label6_image = tk.Label(root,bg="white", image=self.photo6)
        self.label6_image.place(x=800,y=100)

        image_path7 = 'Imagenes\\cuenta-bancaria.png'
        self.image7 = Image.open(image_path7)
        self.photo7 = ImageTk.PhotoImage(self.image7)

        # Crear un widget Label para mostrar la imagen
        self.label7_image = tk.Label(root,bg="white", image=self.photo7)
        self.label7_image.place(x=4,y=170)

        image_path8 = 'Imagenes\\depositar.png'
        self.image8 = Image.open(image_path8)
        self.photo8 = ImageTk.PhotoImage(self.image8)

        # Crear un widget Label para mostrar la imagen
        self.label8_image = tk.Label(root,bg="white", image=self.photo8)
        self.label8_image.place(x=800,y=210)


        image_path2 = 'Imagenes\\dinero.png'
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)

        # Crear un widget Label para mostrar la imagen
        self.label2_image = tk.Label(root,bg="white", image=self.photo2)
        self.label2_image.place(x=4,y=280)

        image_path3 = 'Imagenes\\ganador.png'
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)

        # Crear un widget Label para mostrar la imagen
        self.label3_image = tk.Label(root,bg="white", image=self.photo3)
        self.label3_image.place(x=800,y=340)


        image_path4 = 'Imagenes\\lucro.png'
        self.image4 = Image.open(image_path4)
        self.photo4 = ImageTk.PhotoImage(self.image4)

        # Crear un widget Label para mostrar la imagen
        self.label4_image = tk.Label(root,bg="white", image=self.photo4)
        self.label4_image.place(x=4,y=370)


        self.transacciones_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Gestionar Transacciones", menu=self.transacciones_menu)
        self.transacciones_menu.add_command(label="Realizar Retiro", command=self.interfazDeposito)
        self.transacciones_menu.add_command(label="Realizar Depósito", command=self.interfazDeposito)

        self.consultar_menu = tk.Menu(self.menu, tearoff=0)
        
        self.consultar_menu.add_command(label="Consultar Cuenta", command=self.consultarCuenta)
        self.consultar_menu.add_command(label="Consultar Saldo", command=self.consultarSaldo)
        self.generar_reporte_menu = tk.Menu(self.menu, tearoff=0)
        
        self.menu.add_cascade(label="Generar Reporte", menu=self.generar_reporte_menu)
        self.generar_reporte_menu.add_command(label="Generar", command=self.reporte)

        self.salir_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Salir", menu=self.salir_menu)
        self.salir_menu.add_command(label="Salir", command=self.salir)

        

    def crearCliente(self):
        pass

    def eliminarCliente(self):
        pass

    def crearCuenta(self):
        pass

    def eliminarCuenta(self):
        pass

    def interfazRetiro(self):
        pass

    def interfazDeposito(self):
        pass

    def consultarCliente(self):
        pass

    def consultarCuenta(self):
        pass

    def consultarSaldo(self):
        pass

    def reporte(self):
        pass

    def salir(self):
        pass

    def version(self):
        pass

    def documento(self):
        pass
