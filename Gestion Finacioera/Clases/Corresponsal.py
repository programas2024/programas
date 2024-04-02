import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk 
from Cliente import Cliente
from EliminarCliente import EliminarCliente
from CrearCuenta import CrearCuenta
from EliminarCuenta import EliminarCuenta
from LaTransacciones import LaTransaccion
from ConsultarClientes import MostrarClientes
from ConsultarCuentas import ConsultarCuentas
from ConsultarSaldo import ConsultarSaldo
from Generar import Generar
class Corresponsal:
    def __init__(self, root):
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        root.geometry("900x500")
        root.configure(bg="white")


        image_path = 'Gestion Finacioera\\Imagenes\\bitcoin-con-la-mano.png'
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Crear un widget Label para mostrar la imagen
        self.label_image = tk.Label(root,bg="white", image=self.photo)
        self.label_image.place(x=4,y=50)


        image_path6 = 'Gestion Finacioera\\Imagenes\\control-de-versiones.png'
        self.image6 = Image.open(image_path6)
        self.photo6 = ImageTk.PhotoImage(self.image6)

        # Crear un widget Label para mostrar la imagen
        self.label6_image = tk.Label(root,bg="white", image=self.photo6)
        self.label6_image.place(x=800,y=100)

        image_path61 = 'Gestion Finacioera\\Imagenes\\finaciero imagen.png'
        self.image61 = Image.open(image_path61)
        self.photo61 = ImageTk.PhotoImage(self.image61)

        # Crear un widget Label para mostrar la imagen
        self.label61_image = tk.Label(root,bg="white", image=self.photo61)
        self.label61_image.place(x=200,y=100)

        image_path7 = 'Gestion Finacioera\\Imagenes\\cuenta-bancaria.png'
        self.image7 = Image.open(image_path7)
        self.photo7 = ImageTk.PhotoImage(self.image7)

        # Crear un widget Label para mostrar la imagen
        self.label7_image = tk.Label(root,bg="white", image=self.photo7)
        self.label7_image.place(x=4,y=170)

        image_path8 = 'Gestion Finacioera\\Imagenes\\depositar.png'
        self.image8 = Image.open(image_path8)
        self.photo8 = ImageTk.PhotoImage(self.image8)

        # Crear un widget Label para mostrar la imagen
        self.label8_image = tk.Label(root,bg="white", image=self.photo8)
        self.label8_image.place(x=800,y=210)


        image_path2 = 'Gestion Finacioera\\Imagenes\\dinero.png'
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)

        # Crear un widget Label para mostrar la imagen
        self.label2_image = tk.Label(root,bg="white", image=self.photo2)
        self.label2_image.place(x=4,y=280)

        image_path3 = 'Gestion Finacioera\\Imagenes\\ganador.png'
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)

        # Crear un widget Label para mostrar la imagen
        self.label3_image = tk.Label(root,bg="white", image=self.photo3)
        self.label3_image.place(x=800,y=340)


        image_path4 = 'Gestion Finacioera\\Imagenes\\lucro.png'
        self.image4 = Image.open(image_path4)
        self.photo4 = ImageTk.PhotoImage(self.image4)

        # Crear un widget Label para mostrar la imagen
        self.label4_image = tk.Label(root,bg="white", image=self.photo4)
        self.label4_image.place(x=4,y=370)




        self.gestionar_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Gestionar Clientes", menu=self.gestionar_menu)
        self.gestionar_menu.add_command(label="Crear Cliente", command=self.crearCliente)
        self.gestionar_menu.add_command(label="Eliminar Cliente", command=self.eliminarCliente)
        self.gestionar_menu.add_separator()

        self.cuentas_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Gestionar Cuentas", menu=self.cuentas_menu)
        self.cuentas_menu.add_command(label="Crear Cuenta", command=self.crearCuenta)
        self.cuentas_menu.add_command(label="Eliminar Cuenta", command=self.eliminarCuenta)

        self.transacciones_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Gestionar Transacciones", menu=self.transacciones_menu)
        self.transacciones_menu.add_command(label="Realizar Transaccion", command=self.interfazDeposito)

        self.consultar_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Consultar Información", menu=self.consultar_menu)
        self.consultar_menu.add_command(label="Consultar Cliente", command=self.consultarCliente)
       
        self.consultar_menu.add_command(label="Consultar Cuenta", command=self.consultarCuenta)
        self.consultar_menu.add_command(label="Consultar Saldo", command=self.consultarSaldo)
        self.generar_reporte_menu = tk.Menu(self.menu, tearoff=0)
        
        self.menu.add_cascade(label="Generar Reporte", menu=self.generar_reporte_menu)
        self.generar_reporte_menu.add_command(label="Generar", command=self.reporte)

        self.salir_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Salir", menu=self.salir_menu)
        self.salir_menu.add_command(label="Salir", command=self.salir)

        self.version_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Versión", menu=self.version_menu)
        self.version_menu.add_command(label="Ver Información", command=self.version)
        
        self.documentacion_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Documentación", menu=self.documentacion_menu)
        self.documentacion_menu.add_command(label="Mostrar Código", command=self.documento)

    def crearCliente(self):
       ventana_Corresponsal= tk.Toplevel(self.menu)
       app_Corresponsal = Cliente(ventana_Corresponsal)

    def eliminarCliente(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = EliminarCliente(ventana_Corresponsal)


    def crearCuenta(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = CrearCuenta(ventana_Corresponsal)
        

    def eliminarCuenta(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = EliminarCuenta(ventana_Corresponsal)

    
    def interfazDeposito(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = LaTransaccion(ventana_Corresponsal)


    def consultarCliente(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = MostrarClientes(ventana_Corresponsal)


    def consultarCuenta(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = ConsultarCuentas(ventana_Corresponsal)

    def consultarSaldo(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = ConsultarSaldo(ventana_Corresponsal)


    def reporte(self):
        ventana_Corresponsal= tk.Toplevel(self.menu)
        app_Corresponsal = Generar(ventana_Corresponsal)


    def salir(self):
        pass

    def version(self):
        pass

    def documento(self):
        pass


