# Gestión de Citas Médicas
# Crea un sistema para gestionar citas médicas. El programa debe permitir al usuario registrar pacientes, agendar citas, modificar fechas y consultar las citas existentes. Debe también enviar recordatorios si la cita es dentro de los próximos tres días.
# Requisitos: Manejo de clases, listas, bucles y módulos como datetime.

from datetime import datetime, timedelta

# Clase Paciente


class Paciente:
    def __init__(self, nombre, edad, id_paciente):
        self.nombre = nombre
        self.edad = edad
        self.id_paciente = id_paciente

# Clase Cita


class Cita:
    def __init__(self, paciente, fecha):
        self.paciente = paciente
        self.fecha = fecha

# Clase Sistema de Gestión de Citas


class SistemaCitas:
    def __init__(self):
        self.pacientes = []
        self.citas = []

    # Registrar nuevo paciente
    def registrar_paciente(self, nombre, edad):
        id_paciente = len(self.pacientes) + 1
        paciente = Paciente(nombre, edad, id_paciente)
        self.pacientes.append(paciente)
        print(f"Paciente registrado: {
              paciente.nombre} (ID: {paciente.id_paciente})")

    # Agendar cita
    def agendar_cita(self, id_paciente, fecha_cita):
        paciente = self.buscar_paciente_por_id(id_paciente)
        if paciente:
            cita = Cita(paciente, fecha_cita)
            self.citas.append(cita)
            print(f"Cita agendada para {paciente.nombre} el {
                  fecha_cita.strftime('%Y-%m-%d %H:%M')}")

    # Modificar fecha de una cita
    def modificar_cita(self, id_paciente, nueva_fecha):
        for cita in self.citas:
            if cita.paciente.id_paciente == id_paciente:
                cita.fecha = nueva_fecha
                print(f"Cita modificada para {cita.paciente.nombre} a la nueva fecha: {
                      nueva_fecha.strftime('%Y-%m-%d %H:%M')}")
                return
        print("No se encontró una cita para el paciente con ese ID.")

    # Consultar citas
    def consultar_citas(self):
        if not self.citas:
            print("No hay citas programadas.")
        else:
            print("\n--- Citas Médicas Programadas ---")
            for cita in self.citas:
                print(f"Paciente: {
                      cita.paciente.nombre} - Fecha: {cita.fecha.strftime('%Y-%m-%d %H:%M')}")
            print("--------------------------------")

    # Buscar paciente por ID
    def buscar_paciente_por_id(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id_paciente == id_paciente:
                return paciente
        print(f"No se encontró un paciente con ID {id_paciente}")
        return None

    # Enviar recordatorios para citas dentro de los próximos 3 días
    def enviar_recordatorios(self):
        hoy = datetime.now()
        tres_dias_despues = hoy + timedelta(days=3)

        print("\n--- Recordatorios de Citas Médicas ---")
        for cita in self.citas:
            if hoy <= cita.fecha <= tres_dias_despues:
                print(f"Recordatorio: Cita para {cita.paciente.nombre} el {
                      cita.fecha.strftime('%Y-%m-%d %H:%M')}")
        print("-------------------------------------")


# Función principal para gestionar el sistema
def main():
    sistema = SistemaCitas()

    while True:
        print("\nOpciones: ")
        print("1. Registrar paciente")
        print("2. Agendar cita")
        print("3. Modificar cita")
        print("4. Consultar citas")
        print("5. Enviar recordatorios")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")

        try:
            if opcion == '1':
                nombre = input("Ingresa el nombre del paciente: ")
                edad = int(input("Ingresa la edad del paciente: "))
                sistema.registrar_paciente(nombre, edad)

            elif opcion == '2':
                id_paciente = int(input("Ingresa el ID del paciente: "))
                fecha_str = input(
                    "Ingresa la fecha de la cita (YYYY-MM-DD HH:MM): ")
                fecha_cita = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
                sistema.agendar_cita(id_paciente, fecha_cita)

            elif opcion == '3':
                id_paciente = int(input("Ingresa el ID del paciente: "))
                nueva_fecha_str = input(
                    "Ingresa la nueva fecha de la cita (YYYY-MM-DD HH:MM): ")
                nueva_fecha = datetime.strptime(
                    nueva_fecha_str, "%Y-%m-%d %H:%M")
                sistema.modificar_cita(id_paciente, nueva_fecha)

            elif opcion == '4':
                sistema.consultar_citas()

            elif opcion == '5':
                sistema.enviar_recordatorios()

            elif opcion == '6':
                print("Saliendo del sistema de gestión de citas.")
                break

            else:
                print("Opción inválida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
