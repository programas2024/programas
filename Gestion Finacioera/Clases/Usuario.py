class Usuario:
    def __init__(self, nombre, apellidos, cedula, correo):
        self._nombre = nombre
        self._apellidos = apellidos
        self._cedula = cedula
        self._correo = correo

    # Métodos Getter
    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_cedula(self):
        return self._cedula

    def get_correo(self):
        return self._correo

    # Métodos Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellidos(self, apellidos):
        self._apellidos = apellidos

    def set_cedula(self, cedula):
        self._cedula = cedula

    def set_correo(self, correo):
        self._correo = correo

    # Función toString
    def __str__(self):
        return f"Nombre: {self._nombre}\nApellidos: {self._apellidos}\nCédula: {self._cedula}\nCorreo: {self._correo}"

# Ejemplo de uso
usuario1 = Usuario("Juan", "Perez", "123456789", "juan@example.com")

# Imprimir los detalles del usuario utilizando toString
print(usuario1)
