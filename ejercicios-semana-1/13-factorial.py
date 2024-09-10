# 13. Factorial
# Este programa calcula el factorial de un número proporcionado por el usuario.
num = int(input("Ingresa un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es {factorial}")
