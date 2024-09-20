# Reserva de Hotel
# Implementa un sistema de reservas para un hotel. El programa debe permitir seleccionar la fecha de ingreso, fecha de salida, tipo de habitación, y calcular el costo de la estadía en función de la cantidad de noches. También debe verificar la disponibilidad de habitaciones.
# Requisitos: Manejo de fechas con datetime, clases y herencia (habitaciones simples, dobles, suites).

from datetime import datetime

# Clase base Habitacion


class Habitacion:
    def __init__(self, tipo, precio_por_noche):
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.disponible = True

    def calcular_costo(self, noches):
        return self.precio_por_noche * noches

# Clases derivadas de Habitacion


class HabitacionSimple(Habitacion):
    def __init__(self):
        super().__init__('Simple', 50)


class HabitacionDoble(Habitacion):
    def __init__(self):
        super().__init__('Doble', 80)


class Suite(Habitacion):
    def __init__(self):
        super().__init__('Suite', 150)

# Clase para gestionar el sistema de reservas


class SistemaReservas:
    def __init__(self):
        self.habitaciones = {
            'simple': [HabitacionSimple() for _ in range(5)],
            'doble': [HabitacionDoble() for _ in range(3)],
            'suite': [Suite() for _ in range(2)]
        }

    def verificar_disponibilidad(self, tipo_habitacion):
        for habitacion in self.habitaciones[tipo_habitacion]:
            if habitacion.disponible:
                return habitacion
        return None

    def reservar_habitacion(self, tipo_habitacion, fecha_ingreso, fecha_salida):
        habitacion = self.verificar_disponibilidad(tipo_habitacion)
        if habitacion:
            noches = (fecha_salida - fecha_ingreso).days
            costo_total = habitacion.calcular_costo(noches)
            habitacion.disponible = False
            return habitacion, noches, costo_total
        else:
            raise Exception(f"No hay habitaciones disponibles en la categoría {
                            tipo_habitacion.capitalize()}.")

    def cancelar_reserva(self, habitacion):
        habitacion.disponible = True
        print(f"Reserva de la habitación {habitacion.tipo} cancelada.")


def solicitar_fecha(mensaje):
    fecha_str = input(mensaje)
    return datetime.strptime(fecha_str, "%Y-%m-%d")

# Función principal


def main():
    sistema = SistemaReservas()

    while True:
        print("\nOpciones: ")
        print("1. Realizar reserva")
        print("2. Salir")
        opcion = input("Elige una opción (1-2): ")

        if opcion == '1':
            try:
                tipo_habitacion = input(
                    "Ingresa el tipo de habitación (simple, doble, suite): ").lower()
                if tipo_habitacion not in sistema.habitaciones:
                    print("Tipo de habitación no válido. Intenta de nuevo.")
                    continue

                fecha_ingreso = solicitar_fecha(
                    "Ingresa la fecha de ingreso (YYYY-MM-DD): ")
                fecha_salida = solicitar_fecha(
                    "Ingresa la fecha de salida (YYYY-MM-DD): ")

                if fecha_salida <= fecha_ingreso:
                    print(
                        "La fecha de salida debe ser posterior a la fecha de ingreso.")
                    continue

                habitacion, noches, costo_total = sistema.reservar_habitacion(
                    tipo_habitacion, fecha_ingreso, fecha_salida)
                print(f"\nReserva exitosa: {
                      habitacion.tipo} por {noches} noche(s).")
                print(f"Costo total: ${costo_total:.2f}")

            except Exception as e:
                print(f"Error: {e}")
        elif opcion == '2':
            print("Saliendo del sistema de reservas.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
