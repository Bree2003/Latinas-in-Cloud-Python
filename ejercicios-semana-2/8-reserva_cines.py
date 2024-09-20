# Sistema de Reservas para Cine
# Crea un programa que gestione las reservas para un cine. Los usuarios pueden seleccionar la película, el horario y sus asientos. El sistema debe verificar la disponibilidad de los asientos y generar un boleto con la información de la reserva.
# Requisitos: Manejo de listas, diccionarios y clases.

class Cine:
    def __init__(self, peliculas):
        self.peliculas = peliculas

    # Mostrar cartelera
    def mostrar_cartelera(self):
        print("\n--- Cartelera ---")
        for idx, pelicula in enumerate(self.peliculas):
            print(f"{idx + 1}. {pelicula['titulo']}")
        print("-----------------\n")

    # Seleccionar película por índice
    def seleccionar_pelicula(self, idx):
        return self.peliculas[idx]


class Sala:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.asientos = [['O' for _ in range(columnas)] for _ in range(filas)]

    # Mostrar asientos disponibles
    def mostrar_asientos(self):
        print("\n--- Asientos Disponibles ---")
        for idx, fila in enumerate(self.asientos):
            print(f"Fila {idx + 1}: {' '.join(fila)}")
        print("-----------------------------\n")

    # Verificar disponibilidad de asiento
    def verificar_disponibilidad(self, fila, columna):
        return self.asientos[fila][columna] == 'O'

    # Reservar asiento
    def reservar_asiento(self, fila, columna):
        if self.verificar_disponibilidad(fila, columna):
            self.asientos[fila][columna] = 'X'
            return True
        return False


class Pelicula:
    def __init__(self, titulo, horarios, sala):
        self.titulo = titulo
        self.horarios = horarios
        self.sala = sala

    # Mostrar horarios de la película
    def mostrar_horarios(self):
        print(f"\n--- Horarios para '{self.titulo}' ---")
        for idx, horario in enumerate(self.horarios):
            print(f"{idx + 1}. {horario}")
        print("-------------------------------\n")

    # Seleccionar horario por índice
    def seleccionar_horario(self, idx):
        return self.horarios[idx]


class Reserva:
    def __init__(self, pelicula, horario, asientos):
        self.pelicula = pelicula
        self.horario = horario
        self.asientos = asientos

    # Generar boleto con la información de la reserva
    def generar_boleto(self):
        print("\n--- Boleto de Cine ---")
        print(f"Película: {self.pelicula}")
        print(f"Horario: {self.horario}")
        print(f"Asientos: {', '.join(self.asientos)}")
        print("----------------------\n")


# Función principal
def main():
    # Crear salas de cine
    sala_1 = Sala("Sala 1", 5, 5)
    sala_2 = Sala("Sala 2", 5, 5)

    # Crear películas con horarios y asignarles una sala
    peliculas = [
        {"titulo": "Película A", "obj": Pelicula(
            "Película A", ["14:00", "17:00", "20:00"], sala_1)},
        {"titulo": "Película B", "obj": Pelicula(
            "Película B", ["15:00", "18:00", "21:00"], sala_2)}
    ]

    cine = Cine(peliculas)

    # Proceso de reserva
    while True:
        cine.mostrar_cartelera()
        pelicula_idx = int(input("Selecciona una película por número: ")) - 1
        pelicula_seleccionada = cine.seleccionar_pelicula(pelicula_idx)["obj"]

        pelicula_seleccionada.mostrar_horarios()
        horario_idx = int(input("Selecciona un horario por número: ")) - 1
        horario_seleccionado = pelicula_seleccionada.seleccionar_horario(
            horario_idx)

        pelicula_seleccionada.sala.mostrar_asientos()

        # Reservar asientos
        asientos_reservados = []
        while True:
            fila = int(
                input("Ingresa la fila del asiento (o 0 para terminar): ")) - 1
            if fila == -1:
                break
            columna = int(input("Ingresa la columna del asiento: ")) - 1
            if pelicula_seleccionada.sala.reservar_asiento(fila, columna):
                asientos_reservados.append(
                    f"Fila {fila + 1}, Asiento {columna + 1}")
                print(f"Asiento Fila {
                      fila + 1}, Asiento {columna + 1} reservado con éxito.")
            else:
                print("El asiento ya está ocupado. Intenta con otro.")

        if asientos_reservados:
            # Generar boleto
            reserva = Reserva(pelicula_seleccionada.titulo,
                              horario_seleccionado, asientos_reservados)
            reserva.generar_boleto()

        continuar = input("¿Deseas hacer otra reserva? (s/n): ").lower()
        if continuar != 's':
            break


if __name__ == "__main__":
    main()
