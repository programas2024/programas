

class CalcularPontencia:
    def __init__(self):
        self.resultado_anterior = None

    def calcular_potencia(self, base, exponente):
        resultado = base ** exponente
        self.resultado_anterior = resultado
        return resultado
