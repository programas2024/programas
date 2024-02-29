class Evento:
    def __init__(self, caja, interfaz):
        self.caja = caja
        self.interfaz = interfaz
        self.configurar_eventos()

    def configurar_eventos(self):
        self.caja.bind("<Return>", self.cambiar_caja_enter)
        self.caja.bind("<space>", self.consultar_valor)

    def cambiar_caja_enter(self, event):
        if self.caja == self.interfaz.caja1:
            self.interfaz.cambiar_caja(self.caja, self.interfaz.caja2)
        elif self.caja == self.interfaz.caja2:
            self.interfaz.cambiar_caja(self.caja, self.interfaz.caja3)
        elif self.caja == self.interfaz.caja3:
            self.interfaz.cambiar_caja(self.caja, self.interfaz.caja1)

    def consultar_valor(self, event):
        self.interfaz.consultar()
        self.interfaz.cambiar_caja(self.caja, self.interfaz.caja2)
