#Imprime numeros de 1 a n con while

print("\033[2J\033[H")
print(" --Numeros de 1 al n con While-- ")

n = int(input("Hasta donde ? "))
m = int(input("A que paso ? "))

z = 0

while z <= n:
    print(z, end= " ")
    z = z + m

print(f"\nCiclo Terminado {z}")