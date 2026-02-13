class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")

class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

estudiante1 = Estudiante("Carlos")

estudiante1.mostrar_nombre()