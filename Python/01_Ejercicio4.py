capitalInicial = float(input("Dame el capital inicial: "))
interesAnual = float(input("Dime el ineteres Anual: "))
cantidadAnos = int(input("Dame la cantidad de años: "))

for i in range(0,cantidadAnos):
    capitalInicial += capitalInicial * (interesAnual/100)

print(f"{capitalInicial}")