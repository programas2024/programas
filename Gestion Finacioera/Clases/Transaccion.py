import tkinter as tk
from tkinter import messagebox
from Cuenta import Cuenta

class Transaccion:
    def __init__(self, numero_transaccion, cuenta, monto):
        self._numero_transaccion = numero_transaccion
        self._cuenta = cuenta
        self._monto = monto

    def get_numero_transaccion(self):
        return self._numero_transaccion

    def get_cuenta(self):
        return self._cuenta

    def get_monto(self):
        return self._monto

    
