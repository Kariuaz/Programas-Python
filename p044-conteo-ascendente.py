#Imprime numeros de 1 a 100 con while

print("\033[2J\033[H")
print(" --Numeros de 1 al 100 con While-- ")

z = 1

while z<= 100:
    print(z, end= " ")
    z = z + 1

print(f"\nCiclo Terminado {z}")