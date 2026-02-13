"""

5.- Crear una clase llamada Persona.
con los atributos: nombre, edad

** Un constructor, donde los datos pueden estar vacíos.
** Los setters y getters

para cada uno de los atributos.
*mostrar(): Muestra los datos de la persona.
*es_mayor_de_edad(): Devuelve el valor lógico
indicando si es mayor de edad.
Debe solicitar los datos por la terminal.

"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __init__(self):
        self.nombre = None
        self.edad = None


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_edad(self):
        return self.edad

    def set_edad(self, value):
        self.edad = value

    def mostrar(self):
        print("El nombre de la persona es " , self.nombre , " y la edad es " , self.edad )

    
    def es_mayor_de_edad(self):
        if(self.edad<18):
            print("Es menor de edad")
        else:
            print("es mayor de edad")

    



