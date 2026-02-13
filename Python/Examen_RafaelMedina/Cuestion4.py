

class Pedido:
    def __init__(self, numero_pedido, nombre_cliente, lista_productos, importe_total):
        self.numero_pedido = numero_pedido
        self.nombre_cliente = nombre_cliente
        self.lista_productos = lista_productos
        self.importe_total = importe_total

def calcular_con_iva(lista_productos):
    subtotal = 0
    for producto in lista_productos:
        subtotal += producto["precio"]
    return subtotal * 1.21

registro_pedidos = []

while True:
    num = input("Número de pedido: ")
    nom = input("Nombre del cliente: ")
    
    productos = []
    while True:
        prod = input("Nombre del producto (escriba 'fin' para terminar): ")
        if prod == "fin":
            break
        prec = float(input("Precio: "))
        productos.append({"nombre": prod, "precio": prec})
    
    total = calcular_con_iva(productos)
    nuevo_pedido = Pedido(num, nom, productos, total)
    registro_pedidos.append(nuevo_pedido)
    
    continuar = input("¿Registrar otro pedido? (s/n): ")
    if continuar == "n":
        break

print("\n--- RESUMEN FINAL ---")
for p in registro_pedidos:
    print(f"Pedido: {p.numero_pedido} | Cliente: {p.nombre_cliente} | Total con IVA: {p.importe_total:.2f}")
    for item in p.lista_productos:
        print(f" - {item['nombre']}: {item['precio']}")