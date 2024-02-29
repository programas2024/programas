from Interfaz import Interfaz
import tkinter as tk

class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.app_interface = Interfaz(self.root)
        self.root.mainloop()

Main()