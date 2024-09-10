
# 18. Verificar palíndromo
# Este programa verifica si una cadena proporcionada por el usuario es un palíndromo.
cadena = input("Ingresa una cadena: ")
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")
