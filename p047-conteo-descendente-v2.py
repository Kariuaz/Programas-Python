#Imprime numeros de n a 1 con while

print("\033[2J\033[H")
print(" --Numeros de 1 al n con While-- ")

n = int(input( " Desde donde?: "))
m = int(input("En decremento de: "))
r = n

while r >= 1:
    print(r)
    r = r - m

print(f"\nCiclo terminado: {r}")