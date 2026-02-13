class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

lista_productos = []

while True:
    print("\n1. Registrar Producto")
    print("2. Actualizar Stock")
    print("3. Mostrar Stock Bajo (<5)")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cod = input("Código: ")
        nom = input("Nombre: ")
        while True:
            try:
                prec = float(input("Precio: "))
                stk = int(input("Stock: "))
                nuevo = Producto(cod, nom, prec, stk)
                lista_productos.append(nuevo)
                break
            except ValueError:
                print("Error: Precio y Stock deben ser números.")

    elif opcion == "2":
        buscar = input("Ingrese código del producto: ")
        encontrado = False
        for p in lista_productos:
            if p.codigo == buscar:
                while True:
                    try:
                        nuevo_stock = int(input("Nuevo stock: "))
                        p.stock = nuevo_stock
                        print("Stock actualizado.")
                        encontrado = True
                        break
                    except ValueError:
                        print("El stock debe ser un número entero.")
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "3":
        print("--- Productos con Stock Bajo ---")
        for p in lista_productos:
            if p.stock < 5:
                print(f"Producto: {p.nombre} | Stock: {p.stock}")

    elif opcion == "4":
        break
    
    else:
        print("Opción incorrecta.")


        