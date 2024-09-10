# 15. Tablas de multiplicar
# Este programa imprime la tabla de multiplicar de un número dado por el usuario.
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
