
def calcular_estadisticas(lista):
    total = sum(lista)
    media = total / len(lista)
    mayor = max(lista)
    menor = min(lista)
    dia_mayor = lista.index(mayor) + 1
    dia_menor = lista.index(menor) + 1
    return total, media, dia_mayor, mayor, dia_menor, menor

ventas = []
DIAS_MES = 30

for dia in range(1, DIAS_MES + 1):
    while True:
        try:
            venta = float(input(f"Ventas día {dia}: "))
            if venta < 0:
                print("El valor no puede ser negativo.")
            else:
                ventas.append(venta)
                break
        except ValueError:
            print("Dato no válido. Introduzca un número.")

tot, med, d_max, v_max, d_min, v_min = calcular_estadisticas(ventas)

print(f"\nTotal de ventas: {tot:.2f}")
print(f"Media diaria: {med:.2f}")
print(f"Día con mayor venta: Día {d_max} ({v_max:.2f})")
print(f"Día con menor venta: Día {d_min} ({v_min:.2f})") 



lis