import turtle

class Flor:
    def __init__(self, canvas, x, color_petalos="red", color_tallo="green", color_hojas="dark green", color_contorno="black"):
        self.canvas = canvas
        self.color_petalos = color_petalos
        self.color_tallo = color_tallo
        self.color_hojas = color_hojas
        self.color_contorno = color_contorno
        self.turtle = turtle.RawTurtle(canvas)
        self.turtle.speed(5)
        self.turtle.pensize(2)
        self.x = x  # Posición en el eje X

    def dibujar_petalo(self):
        self.turtle.pencolor(self.color_contorno)  # Contorno negro
        self.turtle.fillcolor(self.color_petalos)
        self.turtle.begin_fill()
        self.turtle.circle(100, 60)
        self.turtle.left(120)
        self.turtle.circle(100, 60)
        self.turtle.left(120)
        self.turtle.end_fill()

    def dibujar_hoja(self, tamaño=70):
        self.turtle.pencolor(self.color_contorno)  # Contorno negro
        self.turtle.fillcolor(self.color_hojas)
        self.turtle.begin_fill()
        self.turtle.circle(tamaño, 60)
        self.turtle.left(120)
        self.turtle.circle(tamaño, 60)
        self.turtle.left(120)
        self.turtle.end_fill()

    def dibujar_flor(self):
        self.turtle.pencolor(self.color_contorno)

        # Mover a una posición inicial centrada para dibujar el tallo y las hojas
        self.turtle.penup()
        self.turtle.goto(self.x, -70)  # Ajusta la posición inicial en Y
        self.turtle.pendown()

        # Dibujar tallo
        self.turtle.pencolor(self.color_tallo)
        self.turtle.pensize(10)  # Ajusta el grosor del tallo
        self.turtle.right(90)
        self.turtle.forward(200)  # Ajusta la longitud del tallo
        self.turtle.left(90)

        # Dibujar hoja a la derecha
        self.turtle.pencolor(self.color_contorno)
        self.turtle.penup()
        self.turtle.goto(self.x + 5, -150)  # Ajusta la posición inicial para la hoja derecha
        self.turtle.pendown()
        self.dibujar_hoja(90)

        # Dibujar hoja a la izquierda
        self.turtle.pencolor(self.color_contorno)
        self.turtle.penup()
        self.turtle.goto(self.x - 65, -250)  # Ajusta la posición inicial para la hoja izquierda
        self.turtle.pendown()
        self.dibujar_hoja(70)

        # Mover a una posición inicial más arriba para dibujar los pétalos
        self.turtle.penup()
        self.turtle.goto(self.x, 0)  # Ajusta la posición inicial en Y para los pétalos
        self.turtle.pendown()

        # Dibujar pétalos
        for _ in range(6):
            self.dibujar_petalo()
            self.turtle.right(60)

    def cambiar_color_rosado(self):
        self.canvas["bg"] = "pink"  # Cambiar el color de fondo directamente

    def cambiar_color_morado(self):
        self.canvas["bg"] = "purple"  # Cambiar el color de fondo directamente

    def mover_flor_suavemente(self):
        self.turtle.hideturtle()  # Oculta la pluma después de dibujar la flor

def main():
    ventana = turtle.Screen()
    ventana.bgcolor("white")
    ventana.setup(width=800, height=600)

    canvas = ventana.getcanvas()

    flor1 = Flor(canvas, x=-200, color_petalos="blue", color_tallo="green", color_hojas="dark turquoise")
    flor2 = Flor(canvas, x=0, color_petalos="red", color_tallo="green", color_hojas="dark green")
    flor3 = Flor(canvas, x=200, color_petalos="orange", color_tallo="green", color_hojas="dark orange")

    flor1.turtle.penup()
    flor1.turtle.pendown()
    flor1.dibujar_flor()

    flor2.turtle.penup()
    flor2.turtle.pendown()
    flor2.dibujar_flor()

    flor3.turtle.penup()
    flor3.turtle.pendown()
    flor3.dibujar_flor()

    # Llamar a la función para cambiar el color a rosado después de 2 segundos
    ventana.ontimer(flor1.cambiar_color_rosado, 2000)

    # Llamar a la función para cambiar el color a morado después de 4 segundos
    ventana.ontimer(flor1.cambiar_color_morado, 4000)

    turtle.done()

if __name__ == "__main__":
    main()














