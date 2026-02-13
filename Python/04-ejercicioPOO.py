class Persona:
    def __init__(self, nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def esMayorDeEdad(self):
        return self.edad >= 18

p = Persona("Rafa", 25)
p.mostrar()
print("¿Es mayor de edad?:", p.esMayorDeEdad())