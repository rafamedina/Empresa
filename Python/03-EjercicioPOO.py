"""
Crea una clase rectangulo con los siguientes atributos:
base
altura
Las clases deben tener los siguientes metodos:
** __init__(self,base, altura) **



"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base*self.altura)
    

    def calcular_perimetro(self):
        return ((self.altura*2)+(self.base*2))
    



base = float(input("dime la base "))
altura = float(input("dime la altura "))

r = Rectangulo(base,altura)

print(r.calcular_area(), "Es el area" )

print(r.calcular_perimetro(), "Es el perimetro" )