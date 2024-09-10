# 5. Intercambio de valores
# Este programa intercambia los valores de dos variables.
a = input("Ingresa el valor de a: ")
b = input("Ingresa el valor de b: ")
# Intercambiamos los valores usando una variable temporal
temp = a
a = b
b = temp
print("Después del intercambio, el valor de a es:", a)
print("Después del intercambio, el valor de b es:", b)
