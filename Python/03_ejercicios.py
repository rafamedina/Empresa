# ==========================================
# EJERCICIO 1: Persona (Nombre, Edad, DNI)
# ==========================================
print("\n--- EJERCICIO 1 ---")

class Persona1:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Solicitud de datos
nom = input("Introduce nombre: ")
eda = int(input("Introduce edad: "))
dni = input("Introduce DNI: ")

p1 = Persona1(nom, eda, dni)

if p1.es_mayor_de_edad():
    print(f"{p1.nombre} es mayor de edad.")
else:
    print(f"{p1.nombre} es menor de edad.")


# ==========================================
# EJERCICIO 2: Rectángulo (Base, Altura)
# ==========================================
print("\n--- EJERCICIO 2 ---")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Solicitud de datos
b = float(input("Introduce la base del rectángulo: "))
h = float(input("Introduce la altura del rectángulo: "))

rect = Rectangulo(b, h)

print(f"El área es: {rect.calcular_area()}")
print(f"El perímetro es: {rect.calcular_perimetro()}")


# ==========================================
# EJERCICIO 3: Libro (Año y Editorial)
# ==========================================
print("\n--- EJERCICIO 3 ---")

class Libro:
    def __init__(self, titulo, autor, editorial, anio):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio

    def verificar_estado(self):
        if self.anio <= 2020:
            return "Antiguo"
        else:
            return "Nuevo"

# Lógica del bucle solicitada:
while True:
    print("Ingresa los datos del libro:")
    t = input("Título: ")
    a = input("Autor: ")
    e = input("Editorial: ")
    y = int(input("Año de publicación: "))
    
    libro = Libro(t, a, e, y)
    estado = libro.verificar_estado()
    
    if estado == "Antiguo":
        print("El libro es antiguo. Fin del proceso.")
        break
    elif estado == "Nuevo":
        if libro.editorial.lower() == "espanola": # Aceptamos mayúsculas o minúsculas
            print("Libro nuevo de editorial Espanola encontrado. Fin del proceso.")
            break
        else:
            print("Es un libro reciente pero la editorial no es 'Espanola'. Intente de nuevo.\n")


# ==========================================
# EJERCICIO 4: Coche (Kilometraje)
# ==========================================
print("\n--- EJERCICIO 4 ---")

class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km

    def km_entrega(self, km_finales):
        self.km = km_finales

# Datos iniciales
print("Registro de alquiler (Inicio):")
marca = input("Marca: ")
mod = input("Modelo: ")
mat = input("Matrícula: ")
km_ini = float(input("Kilometraje Inicial: "))

auto = Coche(marca, mod, mat, km_ini)
print("Estado Inicial:", auto.__dict__)

# Datos finales
km_fin = float(input("\nIngrese el Kilometraje de entrega (Final): "))
auto.km_entrega(km_fin)
print("Estado Final:", auto.__dict__)


# ==========================================
# EJERCICIO 5: Persona (Getters y Setters)
# ==========================================
print("\n--- EJERCICIO 5 ---")

class PersonaFull:
    def __init__(self, nombre="", edad=0):
        self.__nombre = nombre
        self.__edad = edad

    # Setters y Getters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    # Métodos
    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18

# Uso por terminal
print("Creando persona...")
nom_in = input("Nombre: ")
eda_in = int(input("Edad: "))

p5 = PersonaFull() # Inicia vacío según constructor
p5.set_nombre(nom_in) # Usamos setter
p5.set_edad(eda_in)   # Usamos setter

p5.mostrar()
print(f"¿Es mayor de edad?: {p5.es_mayor_de_edad()}")



