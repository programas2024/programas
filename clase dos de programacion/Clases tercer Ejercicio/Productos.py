class Producto:
    def __init__(self):
        self.nombre_producto = ""
        self.valor_original = 0
        self.descuento_porcentaje = 0

    def aplicar_descuento(self):
        descuento = self.valor_original * (self.descuento_porcentaje / 100)
        valor_a_pagar = self.valor_original - descuento
        return descuento, valor_a_pagar
