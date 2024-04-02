from Deposito import Deposito

class Cuenta:
    def __init__(self, numero_cuenta, saldo, cedula_cliente):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo
        self._cedula_cliente = cedula_cliente

    def get_numero_cuenta(self):
        return self._numero_cuenta

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo += monto

