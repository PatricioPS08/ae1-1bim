# Listas para almacenar los datos de cada venta
nombres = []
apellidos = []
cantidades = []
precios = []
totales = []

def calcular_descuento(cantidad, subtotal):
    if cantidad == 1:
        return subtotal * 0.10
    elif cantidad == 2:
        return subtotal * 0.20
    elif cantidad == 3:
        return subtotal * 0.40
    elif cantidad > 3:
        return subtotal * 0.60
    else:
        return 0

while True:
    print("\n--- Registro de nueva venta ---")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")

    try:
        cantidad = int(input("Ingrese la cantidad de trajes: "))
        precio_unitario = float(input("Ingrese el precio unitario del traje: "))
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números válidos.")
        continue

    # Cálculos
    subtotal = cantidad * precio_unitario
    descuento = calcular_descuento(cantidad, subtotal)
    total = subtotal - descuento

    # Almacenar datos
    nombres.append(nombre)
    apellidos.append(apellido)
    cantidades.append(cantidad)
    precios.append(precio_unitario)
    totales.append(total)

    print(f"\nResumen de la venta para {nombre} {apellido}:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")

    # Verificar si el usuario quiere continuar
    continuar = input("\n¿Desea registrar otra venta? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todas las ventas registradas
print("\n=== Resumen de Ventas Registradas ===")
for i in range(len(nombres)):
    print(f"\nCliente: {nombres[i]} {apellidos[i]}")
    print(f"Cantidad de trajes: {cantidades[i]}")
    print(f"Precio unitario: ${precios[i]:.2f}")
    print(f"Total pagado: ${totales[i]:.2f}")

# Cálculo del promedio, venta más alta y más baja
if totales:
    promedio = sum(totales) / len(totales)
    venta_max = max(totales)
    venta_min = min(totales)

    print(f"\nPromedio de ventas: ${promedio:.2f}")
    print(f"Venta más alta: ${venta_max:.2f}")
    print(f"Venta más baja: ${venta_min:.2f}")
else:
    print("No se registraron ventas.")