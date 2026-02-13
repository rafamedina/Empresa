class Persona:
    # Constructor con valores por defecto
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    # Setters y Getters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    # Métodos solicitados
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

# --- Bloque principal para pedir datos por terminal ---

# Solicitamos los datos
nombre_input = input("Introduce el nombre: ")
edad_input = int(input("Introduce la edad: "))

# Creamos el objeto usando el constructor
p = Persona(nombre_input, edad_input)

# Ejecutamos los métodos
p.mostrar()
print("¿Es mayor de edad?:", p.es_mayor_de_edad())