from Interfaz import Interfaz
from Productos import Producto
import tkinter as tk

class Main:
    def __init__(self):
        logica_producto = Producto()
        self.root = tk.Tk()
        self.app_interface = Interfaz(self.root, logica_producto)
        self.root.mainloop()

Main()