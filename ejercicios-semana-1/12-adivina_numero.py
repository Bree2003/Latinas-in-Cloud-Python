# 12. Adivina el número
# Este programa hace que el usuario adivine un número entre 1 y 10.
import random
numero_secreto = random.randint(1, 10)
adivinanza = int(input("Adivina un número entre 1 y 10: "))
if adivinanza == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"No adivinaste. El número era {numero_secreto}.")
