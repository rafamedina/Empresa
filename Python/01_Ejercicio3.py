salario = float(input("Dime el salario del empleado: "))

if salario > 1000:
    salario += salario * 0.1
    

print(f"El salario es de: {salario}")