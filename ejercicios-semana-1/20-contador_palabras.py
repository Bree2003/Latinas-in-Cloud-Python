# 20. Contador de palabras
# Este programa cuenta el número de palabras en una frase proporcionada por el usuario.
frase = input("Ingresa una frase: ")
palabras = frase.split()
num_palabras = len(palabras)
print("El número de palabras en la frase es:", num_palabras)
