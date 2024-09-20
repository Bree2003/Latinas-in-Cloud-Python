# 1.Caja Registradora
# Crea un programa que simule una caja registradora. El programa debe permitir ingresar productos (nombre, cantidad, precio), calcular el total de la compra, aplicar descuentos si el cliente tiene una tarjeta de fidelización y mostrar un recibo detallado.
# Requisitos: Manejo de listas, diccionarios, bucles y funciones.

# *función para agregar un producto al carrito
def agregar_producto(carrito):
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad: "))
    precio = float(input("Ingresa el precio unitario: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "total": cantidad * precio
    }

    carrito.append(producto)
    print(f"{cantidad}x {nombre} agregado(s) al carrito.\n")

# *función para calcular el total


def calcular_total(carrito):
    total = sum(producto['total'] for producto in carrito)
    return total

# *función para aplicar descuento si tiene tarjeta de fidelización


def aplicar_descuento(total, tiene_tarjeta):
    if tiene_tarjeta:
        print("Aplicando un 10% de descuento por tarjeta de fidelización...")
        total *= 0.90  # aplica un 10% de descuento
    return total

# *función para mostrar el recibo


def mostrar_recibo(carrito, total, tiene_tarjeta):
    print("\n----- Recibo -----")
    for producto in carrito:
        print(f"{producto['cantidad']}x {producto['nombre']} - ${producto['precio']:.2f} c/u - Total: ${producto['total']:.2f}")

    if tiene_tarjeta:
        print("Descuento aplicado: 10%")

    print(f"\nTotal a pagar: ${total:.2f}")
    print("------------------\n")

# *función principal


def caja_registradora():
    carrito = []
    while True:
        agregar_producto(carrito)

        continuar = input("¿Deseas agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    total = calcular_total(carrito)
    tiene_tarjeta = input(
        "¿El cliente tiene tarjeta de fidelización? (s/n): ").lower() == 's'

    total_con_descuento = aplicar_descuento(total, tiene_tarjeta)
    mostrar_recibo(carrito, total_con_descuento, tiene_tarjeta)


# ejecutar el programa
caja_registradora()
