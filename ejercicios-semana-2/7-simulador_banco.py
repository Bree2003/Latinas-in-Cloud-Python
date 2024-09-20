# Simulador de Banco
# Desarrolla un simulador de banco que permita a los usuarios crear cuentas, hacer depósitos, retiros y consultar su saldo. Debe también permitir la transferencia de dinero entre cuentas y llevar un historial de transacciones.
# Requisitos: Clases, listas, manejo de excepciones y archivos.

import json
import os

# Clase para la cuenta bancaria


class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial
        self.historial = []

    # Realizar un depósito
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.saldo += monto
        self.historial.append(f"Depósito: +${monto}")
        print(f"Depósito de ${
              monto} realizado con éxito. Nuevo saldo: ${self.saldo}")

    # Realizar un retiro
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= monto
        self.historial.append(f"Retiro: -${monto}")
        print(f"Retiro de ${
              monto} realizado con éxito. Nuevo saldo: ${self.saldo}")

    # Consultar saldo
    def consultar_saldo(self):
        print(f"El saldo de la cuenta {self.numero_cuenta} es: ${self.saldo}")

    # Transferir dinero a otra cuenta
    def transferir(self, cuenta_destino, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= monto
        cuenta_destino.saldo += monto
        self.historial.append(
            f"Transferencia enviada: -${monto} a la cuenta {cuenta_destino.numero_cuenta}")
        cuenta_destino.historial.append(
            f"Transferencia recibida: +${monto} de la cuenta {self.numero_cuenta}")
        print(f"Transferencia de ${monto} realizada con éxito a la cuenta {
              cuenta_destino.numero_cuenta}.")

    # Ver historial de transacciones
    def ver_historial(self):
        print(f"\n--- Historial de la cuenta {self.numero_cuenta} ---")
        for transaccion in self.historial:
            print(transaccion)
        print("------------------------------------------")


# Clase para el banco que gestiona cuentas bancarias
class Banco:
    def __init__(self, archivo_cuentas):
        self.archivo_cuentas = archivo_cuentas
        self.cuentas = self.cargar_datos()

    # Cargar datos desde un archivo
    def cargar_datos(self):
        if os.path.exists(self.archivo_cuentas):
            with open(self.archivo_cuentas, 'r') as f:
                datos = json.load(f)
                # Reconstruir cuentas desde los datos
                cuentas = {}
                for num_cuenta, info in datos.items():
                    cuenta = CuentaBancaria(
                        num_cuenta, info['nombre_titular'], info['saldo'])
                    cuenta.historial = info['historial']
                    cuentas[num_cuenta] = cuenta
                return cuentas
        else:
            return {}

    # Guardar datos en un archivo
    def guardar_datos(self):
        datos = {}
        for num_cuenta, cuenta in self.cuentas.items():
            datos[num_cuenta] = {
                'nombre_titular': cuenta.nombre_titular,
                'saldo': cuenta.saldo,
                'historial': cuenta.historial
            }
        with open(self.archivo_cuentas, 'w') as f:
            json.dump(datos, f, indent=4)

    # Crear una nueva cuenta
    def crear_cuenta(self, numero_cuenta, nombre_titular, saldo_inicial=0):
        if numero_cuenta in self.cuentas:
            raise Exception(f"La cuenta con el número {
                            numero_cuenta} ya existe.")
        nueva_cuenta = CuentaBancaria(
            numero_cuenta, nombre_titular, saldo_inicial)
        self.cuentas[numero_cuenta] = nueva_cuenta
        self.guardar_datos()
        print(f"Cuenta creada con éxito. Número de cuenta: {numero_cuenta}, Titular: {
              nombre_titular}, Saldo inicial: ${saldo_inicial}")

    # Buscar cuenta por número de cuenta
    def buscar_cuenta(self, numero_cuenta):
        if numero_cuenta not in self.cuentas:
            raise Exception(f"No se encontró ninguna cuenta con el número {
                            numero_cuenta}.")
        return self.cuentas[numero_cuenta]


# Función principal
def main():
    banco = Banco('cuentas.json')

    while True:
        print("\nOpciones:")
        print("1. Crear cuenta")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Transferir dinero")
        print("5. Consultar saldo")
        print("6. Ver historial de transacciones")
        print("7. Salir")
        opcion = input("Elige una opción (1-7): ")

        try:
            if opcion == '1':
                numero_cuenta = input("Ingresa el número de cuenta: ")
                nombre_titular = input("Ingresa el nombre del titular: ")
                saldo_inicial = float(
                    input("Ingresa el saldo inicial (opcional): ") or 0)
                banco.crear_cuenta(
                    numero_cuenta, nombre_titular, saldo_inicial)

            elif opcion == '2':
                numero_cuenta = input(
                    "Ingresa el número de cuenta para el depósito: ")
                cuenta = banco.buscar_cuenta(numero_cuenta)
                monto = float(input("Ingresa el monto a depositar: "))
                cuenta.depositar(monto)
                banco.guardar_datos()

            elif opcion == '3':
                numero_cuenta = input(
                    "Ingresa el número de cuenta para el retiro: ")
                cuenta = banco.buscar_cuenta(numero_cuenta)
                monto = float(input("Ingresa el monto a retirar: "))
                cuenta.retirar(monto)
                banco.guardar_datos()

            elif opcion == '4':
                cuenta_origen = input(
                    "Ingresa el número de cuenta de origen: ")
                cuenta_destino = input(
                    "Ingresa el número de cuenta de destino: ")
                monto = float(input("Ingresa el monto a transferir: "))
                cuenta_origen_obj = banco.buscar_cuenta(cuenta_origen)
                cuenta_destino_obj = banco.buscar_cuenta(cuenta_destino)
                cuenta_origen_obj.transferir(cuenta_destino_obj, monto)
                banco.guardar_datos()

            elif opcion == '5':
                numero_cuenta = input(
                    "Ingresa el número de cuenta para consultar el saldo: ")
                cuenta = banco.buscar_cuenta(numero_cuenta)
                cuenta.consultar_saldo()

            elif opcion == '6':
                numero_cuenta = input(
                    "Ingresa el número de cuenta para ver el historial: ")
                cuenta = banco.buscar_cuenta(numero_cuenta)
                cuenta.ver_historial()

            elif opcion == '7':
                print("Saliendo del sistema bancario.")
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
