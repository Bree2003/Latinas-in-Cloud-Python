# 14. Números pares en una lista
# Este programa imprime todos los números pares en una lista dada.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print("Los números pares en la lista son:", pares)
