#Permite al usuario adivinar un numero generado al azar

import random

print("\033[2J\033[H")
print(" --Permite al usuario adivinar un numero generado al azar entre 1 y 50-- ")

n = random.randint(1,50)

ci = 0

while True:
    i = int(input("Tu numero: "))
    ci += 1
    if i < n:
        print(f"Demasiado bajo")
    elif i > n:
        print(f"Demasiado alto")
    else:
        print("Adivinaste el numero secreto {n}")
        print(f"Usaste {ci} intentos")




