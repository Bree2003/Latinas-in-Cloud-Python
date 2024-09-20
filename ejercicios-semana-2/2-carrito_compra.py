# Carrito de Compras
# Desarrolla una aplicación de carrito de compras. Los usuarios pueden agregar productos al carrito, eliminar productos, y actualizar la cantidad de los mismos. Al finalizar la compra, se debe mostrar el total a pagar, incluyendo impuestos.
# Requisitos: Uso de clases para representar el carrito y los productos, manejo de excepciones.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        if producto.nombre in self.productos:
            self.productos[producto.nombre]['cantidad'] += cantidad
        else:
            self.productos[producto.nombre] = {
                'producto': producto, 'cantidad': cantidad}
        print(f"Producto agregado: {producto.nombre}, Cantidad: {cantidad}")

    def eliminar_producto(self, nombre_producto):
        if nombre_producto not in self.productos:
            raise KeyError(f"No se encontró el producto '{
                           nombre_producto}' en el carrito.")

        del self.productos[nombre_producto]
        print(f"Producto eliminado: {nombre_producto}")

    def actualizar_cantidad(self, nombre_producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        if nombre_producto not in self.productos:
            raise KeyError(f"No se encontró el producto '{
                           nombre_producto}' en el carrito.")

        self.productos[nombre_producto]['cantidad'] = cantidad
        print(f"Cantidad actualizada: {
              nombre_producto}, Nueva cantidad: {cantidad}")

    def calcular_total(self, impuesto=0.19):
        total = 0
        for item in self.productos.values():
            total += item['producto'].precio * item['cantidad']

        total_con_impuesto = total * (1 + impuesto)
        return total_con_impuesto

    def mostrar_carrito(self):
        print("\n--- Carrito de Compras ---")
        for item in self.productos.values():
            nombre = item['producto'].nombre
            cantidad = item['cantidad']
            precio = item['producto'].precio
            print(f"{nombre}: {cantidad}x ${precio:.2f} c/u")
        print("--------------------------\n")


def main():
    carrito = Carrito()

    while True:
        print("\nOpciones: ")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Ver carrito")
        print("5. Finalizar compra")
        opcion = input("Elige una opción (1-5): ")

        try:
            if opcion == '1':
                nombre = input("Ingresa el nombre del producto: ")
                precio = float(input("Ingresa el precio del producto: "))
                cantidad = int(input("Ingresa la cantidad: "))

                producto = Producto(nombre, precio)
                carrito.agregar_producto(producto, cantidad)

            elif opcion == '2':
                nombre_producto = input(
                    "Ingresa el nombre del producto a eliminar: ")
                carrito.eliminar_producto(nombre_producto)

            elif opcion == '3':
                nombre_producto = input(
                    "Ingresa el nombre del producto a actualizar: ")
                cantidad = int(input("Ingresa la nueva cantidad: "))
                carrito.actualizar_cantidad(nombre_producto, cantidad)

            elif opcion == '4':
                carrito.mostrar_carrito()

            elif opcion == '5':
                total = carrito.calcular_total()
                carrito.mostrar_carrito()
                print(f"Total con impuestos: ${total:.2f}")
                break

            else:
                print("Opción inválida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
