from Tooltip import Tooltip
import tkinter as tk
from tkinter import*
from tkinter import messagebox
class Registro:

    def mostraAyuda(self,event):
            messagebox.showinfo("Ayuda","Debe diligenciar todos los campos y luego precione el boton registrarse")

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("REGISTRO")
        self.ventana.geometry("500x500")


        self.laberTItulo=tk.Label(self.ventana,text="REGISTRARSE",fg="black",border=0)
        self.laberTItulo.place(x=130,y=40)

        self.labernombre=tk.Label(self.ventana,text="NOMBRE",fg="black",border=0)
        self.labernombre.place(x=130,y=70)

        self.caja_nombre = tk.Entry(self.ventana)
        self.caja_nombre.place(x=210, y=70)

        self.laberApellidos=tk.Label(self.ventana,text="APELLIDOS",fg="black",border=0)
        self.laberApellidos.place(x=130,y=100)

        self.caja_apellidos = tk.Entry(self.ventana)
        self.caja_apellidos.place(x=210, y=100)

        self.laberCedula=tk.Label(self.ventana,text="CEDULA",fg="black",border=0)
        self.laberCedula.place(x=130,y=130)

        self.caja_cedula = tk.Entry(self.ventana)
        self.caja_cedula.place(x=210, y=130)

        self.laberCedula=tk.Label(self.ventana,text="TELEFONO",fg="black",border=0)
        self.laberCedula.place(x=130,y=160)

        self.caja_cedula = tk.Entry(self.ventana)
        self.caja_cedula.place(x=210, y=160)

        self.laberCedula=tk.Label(self.ventana,text="CORREO",fg="black",border=0)
        self.laberCedula.place(x=130,y=190)

        self.caja_cedula = tk.Entry(self.ventana)
        self.caja_cedula.place(x=210, y=190)

        self.Ayuda_button = tk.Button(self.ventana, text="AYUDA", command=self.ayuda,border=1)
        self.Ayuda_button.place(x=370, y=60, width=100)
        Tooltip(self.Ayuda_button,"Obten ayuda")
        self.Ayuda_button.bind('<Button-1>',self.mostraAyuda)

        
        self.registrase_button = tk.Button(self.ventana, text="REGISTRARSE", command=self.registrase)
        self.registrase_button.place(x=170, y=250, width=100)

        self.registrase_button = tk.Button(self.ventana, text="CANCELAR", command=self.cancelar)
        self.registrase_button.place(x=290, y=250, width=100)

        self.ventana.bind('<Alt-a>',self.mostraAyuda)

        self.ventana.mainloop()




    def registrase(self):
        pass

    def ayuda(self):
        pass

    def cancelar(self):
        self.ventana.destroy()
app=Registro()












        


