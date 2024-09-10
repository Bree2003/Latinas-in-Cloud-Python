
# 17. Suma de dígitos
# Este programa suma los dígitos de un número entero proporcionado por el usuario.
num = input("Ingresa un número entero: ")
suma = sum(int(digito) for digito in num)
print("La suma de los dígitos es:", suma)
