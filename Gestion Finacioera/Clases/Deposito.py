import datetime

class Deposito:
    def __init__(self, numero_transaccion, cuenta_manager, monto):
        self._numero_transaccion = numero_transaccion
        self._cuenta_manager = cuenta_manager
        self._monto = monto
        self._fecha_hora = None

    def get_numero_transaccion(self):
        return self._numero_transaccion

    def get_monto(self):
        return self._monto

    def realizar_deposito(self):
        cuenta = self._cuenta_manager.buscar_cuenta()

        if cuenta is not None:
            cuenta.depositar(self._monto)
            self._fecha_hora = datetime.datetime.now()
            return f"Depósito exitoso. Monto: {self._monto}. Recibo:\nFecha y Hora: {self._fecha_hora}\nNúmero de Cuenta: {self.ocultar_ultimos_digitos(cuenta.get_numero_cuenta())}"
        else:
            return "Error: La cuenta no existe."

    def ocultar_ultimos_digitos(self, numero_cuenta):
        return "*" * (len(numero_cuenta) - 5) + numero_cuenta[-5:]

    def __str__(self):
        return f"Número de Transacción: {self._numero_transaccion}\nMonto: {self._monto}"
