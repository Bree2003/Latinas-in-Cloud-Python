# Gestión de Biblioteca
# Implementa un programa para gestionar una biblioteca. El sistema debe permitir registrar libros, prestar libros a usuarios, y llevar un control de los libros prestados y su fecha de devolución. Los libros deben ser devueltos antes de una fecha límite, o el programa aplicará multas.
# Requisitos: Clases, manejo de fechas y archivos.

import json
import os
from datetime import datetime, timedelta

# Clase para el sistema de la biblioteca


class Biblioteca:
    def __init__(self, archivo_libros, archivo_prestamos):
        self.archivo_libros = archivo_libros
        self.archivo_prestamos = archivo_prestamos
        self.libros = self.cargar_datos(self.archivo_libros)
        self.prestamos = self.cargar_datos(self.archivo_prestamos)

    # Cargar datos desde archivos
    def cargar_datos(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                return json.load(f)
        else:
            return {}

    # Guardar datos en archivos
    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    # Registrar un nuevo libro
    def registrar_libro(self, titulo, autor, ejemplares):
        if titulo in self.libros:
            raise Exception(f"El libro '{titulo}' ya está registrado.")
        self.libros[titulo] = {
            'autor': autor,
            'ejemplares': ejemplares,
            'prestados': 0
        }
        self.guardar_datos(self.archivo_libros, self.libros)
        print(f"Libro '{titulo}' registrado con éxito.")

    # Prestar un libro a un usuario
    def prestar_libro(self, titulo, usuario, dias_prestamo=7):
        if titulo not in self.libros:
            raise Exception(
                f"El libro '{titulo}' no está disponible en la biblioteca.")
        if self.libros[titulo]['prestados'] >= self.libros[titulo]['ejemplares']:
            raise Exception(
                f"No hay ejemplares disponibles del libro '{titulo}'.")

        fecha_prestamo = datetime.now()
        fecha_devolucion = fecha_prestamo + timedelta(days=dias_prestamo)

        self.prestamos[usuario] = {
            'titulo': titulo,
            'fecha_prestamo': fecha_prestamo.strftime('%Y-%m-%d'),
            'fecha_devolucion': fecha_devolucion.strftime('%Y-%m-%d'),
            'devuelto': False
        }

        self.libros[titulo]['prestados'] += 1
        self.guardar_datos(self.archivo_libros, self.libros)
        self.guardar_datos(self.archivo_prestamos, self.prestamos)
        print(f"Libro '{titulo}' prestado a {usuario}. Fecha de devolución: {
              fecha_devolucion.strftime('%Y-%m-%d')}")

    # Devolver un libro
    def devolver_libro(self, usuario):
        if usuario not in self.prestamos:
            raise Exception(f"El usuario {usuario} no tiene libros prestados.")

        prestamo = self.prestamos[usuario]
        titulo = prestamo['titulo']
        fecha_devolucion = datetime.strptime(
            prestamo['fecha_devolucion'], '%Y-%m-%d')
        fecha_actual = datetime.now()

        if fecha_actual > fecha_devolucion:
            dias_retraso = (fecha_actual - fecha_devolucion).days
            multa = dias_retraso * 1  # Multa de $1 por día de retraso
            print(f"El libro '{titulo}' se devolvió con {
                  dias_retraso} días de retraso. Multa: ${multa}")
        else:
            print(f"El libro '{titulo}' se devolvió a tiempo. No hay multa.")

        self.libros[titulo]['prestados'] -= 1
        del self.prestamos[usuario]

        self.guardar_datos(self.archivo_libros, self.libros)
        self.guardar_datos(self.archivo_prestamos, self.prestamos)
        print(f"Libro '{titulo}' devuelto por {usuario}.")

    # Ver libros disponibles
    def ver_libros_disponibles(self):
        print("\n--- Libros disponibles ---")
        for titulo, datos in self.libros.items():
            disponibles = datos['ejemplares'] - datos['prestados']
            print(
                f"{titulo} ({disponibles} disponibles) - Autor: {datos['autor']}")
        print("---------------------------")

    # Ver libros prestados
    def ver_prestamos(self):
        print("\n--- Libros prestados ---")
        for usuario, prestamo in self.prestamos.items():
            print(f"Usuario: {usuario}")
            print(f"  Libro: {prestamo['titulo']}")
            print(f"  Fecha de préstamo: {prestamo['fecha_prestamo']}")
            print(f"  Fecha de devolución: {prestamo['fecha_devolucion']}")
            print(f"  Devuelto: {'Sí' if prestamo['devuelto'] else 'No'}")
        print("--------------------------")


# Función principal
def main():
    biblioteca = Biblioteca('libros.json', 'prestamos.json')

    while True:
        print("\nOpciones:")
        print("1. Registrar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Ver libros disponibles")
        print("5. Ver libros prestados")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")

        try:
            if opcion == '1':
                titulo = input("Ingresa el título del libro: ")
                autor = input("Ingresa el autor del libro: ")
                ejemplares = int(input("Ingresa la cantidad de ejemplares: "))
                biblioteca.registrar_libro(titulo, autor, ejemplares)

            elif opcion == '2':
                titulo = input("Ingresa el título del libro a prestar: ")
                usuario = input("Ingresa el nombre del usuario: ")
                dias_prestamo = int(
                    input("Ingresa la cantidad de días para el préstamo (predeterminado: 7): ") or 7)
                biblioteca.prestar_libro(titulo, usuario, dias_prestamo)

            elif opcion == '3':
                usuario = input(
                    "Ingresa el nombre del usuario que devuelve el libro: ")
                biblioteca.devolver_libro(usuario)

            elif opcion == '4':
                biblioteca.ver_libros_disponibles()

            elif opcion == '5':
                biblioteca.ver_prestamos()

            elif opcion == '6':
                print("Saliendo del sistema de biblioteca.")
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
