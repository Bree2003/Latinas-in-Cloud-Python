# Sistema de Inventario para Tienda
# Desarrolla un sistema de inventario para una tienda. El programa debe permitir ingresar nuevos productos, actualizar el stock de productos existentes, y realizar búsquedas por nombre o categoría. También debe generar reportes de productos agotados.
# Requisitos: Uso de archivos para guardar los datos, manejo de diccionarios y excepciones.

import json
import os

# Clase para el sistema de inventario


class SistemaInventario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = self.cargar_datos()

    # Cargar datos desde el archivo
    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        else:
            return {}

    # Guardar datos en el archivo
    def guardar_datos(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.productos, f, indent=4)

    # Agregar un nuevo producto
    def agregar_producto(self, nombre, categoria, stock, precio):
        if nombre in self.productos:
            raise Exception(f"El producto '{nombre}' ya existe.")
        self.productos[nombre] = {
            'categoria': categoria,
            'stock': stock,
            'precio': precio
        }
        self.guardar_datos()
        print(f"Producto '{nombre}' agregado con éxito.")

    # Actualizar el stock de un producto
    def actualizar_stock(self, nombre, nuevo_stock):
        if nombre not in self.productos:
            raise Exception(f"El producto '{nombre}' no existe.")
        self.productos[nombre]['stock'] = nuevo_stock
        self.guardar_datos()
        print(f"Stock del producto '{nombre}' actualizado a {nuevo_stock}.")

    # Buscar producto por nombre
    def buscar_por_nombre(self, nombre):
        producto = self.productos.get(nombre)
        if producto:
            self.mostrar_producto(nombre, producto)
        else:
            print(f"El producto '{nombre}' no fue encontrado.")

    # Buscar productos por categoría
    def buscar_por_categoria(self, categoria):
        encontrados = {k: v for k, v in self.productos.items()
                       if v['categoria'] == categoria}
        if encontrados:
            print(f"\n--- Productos en la categoría '{categoria}' ---")
            for nombre, datos in encontrados.items():
                self.mostrar_producto(nombre, datos)
            print("----------------------------------------------")
        else:
            print(f"No se encontraron productos en la categoría '{
                  categoria}'.")

    # Generar reporte de productos agotados
    def reporte_productos_agotados(self):
        agotados = {k: v for k, v in self.productos.items() if v['stock'] == 0}
        if agotados:
            print("\n--- Reporte de productos agotados ---")
            for nombre, datos in agotados.items():
                self.mostrar_producto(nombre, datos)
            print("-------------------------------------")
        else:
            print("No hay productos agotados.")

    # Mostrar información de un producto
    def mostrar_producto(self, nombre, datos):
        print(f"Nombre: {nombre}")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Stock: {datos['stock']}")
        print(f"  Precio: ${datos['precio']:.2f}\n")


# Función principal
def main():
    sistema = SistemaInventario('inventario.json')

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Buscar producto por nombre")
        print("4. Buscar productos por categoría")
        print("5. Generar reporte de productos agotados")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")

        try:
            if opcion == '1':
                nombre = input("Ingresa el nombre del producto: ")
                categoria = input("Ingresa la categoría del producto: ")
                stock = int(input("Ingresa el stock inicial: "))
                precio = float(input("Ingresa el precio del producto: "))
                sistema.agregar_producto(nombre, categoria, stock, precio)

            elif opcion == '2':
                nombre = input("Ingresa el nombre del producto a actualizar: ")
                nuevo_stock = int(input("Ingresa el nuevo stock: "))
                sistema.actualizar_stock(nombre, nuevo_stock)

            elif opcion == '3':
                nombre = input(
                    "Ingresa el nombre del producto que deseas buscar: ")
                sistema.buscar_por_nombre(nombre)

            elif opcion == '4':
                categoria = input("Ingresa la categoría que deseas buscar: ")
                sistema.buscar_por_categoria(categoria)

            elif opcion == '5':
                sistema.reporte_productos_agotados()

            elif opcion == '6':
                print("Saliendo del sistema de inventario.")
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
