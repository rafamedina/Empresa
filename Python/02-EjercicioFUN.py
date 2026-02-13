import math
# def funcion():
#     distancia = float(input("Dime la distancia "))
#     velocidad = float(input("Dime la velocidad "))
#     return distancia / velocidad


# print(funcion())



def function():
    medida = input("Dime la unidad (milimetros / decimetros / centimetros /metros): ").lower()

    R = float(input("Dime el radio: "))
    altura = float(input("Dime la altura del cilindro: "))

    volumen = math.pi * (R**2) * altura

    if medida == "milimetros":
        volumen = volumen / 1000000000
    elif medida == "decimetros":
        volumen = volumen / 1000
    elif medida == "centimetros":
        volumen = volumen / 1000000
    elif medida == "metros":
        pass   
    else:
        raise ValueError("Unidad no válida")
    print(f"El resultado es {volumen:.2f} {medida} ")


function()

