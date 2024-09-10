# 11. Contador de vocales
# Este programa cuenta el número de vocales en una cadena proporcionada por el usuario.
cadena = input("Ingresa una cadena: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print("El número de vocales en la cadena es:", contador)
