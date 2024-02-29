class Acumulativa:
    def __init__(self):
        self.valor_acumulado = 0

    def agregar_numero(self, numero):
        self.valor_acumulado += numero

    def obtener_resultado(self):
        return self.valor_acumulado
