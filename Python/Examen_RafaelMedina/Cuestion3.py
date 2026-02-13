

class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def consultar_saldo(self):
        print(f"Su saldo actual es: {self.saldo}")

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print("Dinero ingresado correctamente.")

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("Operación denegada: No tiene saldo suficiente.")
        else:
            self.saldo -= cantidad
            print("Retiro exitoso.")

cuenta = CuentaBancaria(1000)

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cuenta.consultar_saldo()
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.ingresar_dinero(cantidad)
    elif opcion == "3":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar_dinero(cantidad)
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción no válida.")