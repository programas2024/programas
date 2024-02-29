import tkinter as tk

class Limpiar():
    def __init__(self, cajas):
        self.cajas = cajas

    def limpiar(self):
        for caja in self.cajas:
            caja.config(state='normal')
            caja.delete(0, tk.END)