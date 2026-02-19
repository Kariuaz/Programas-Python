#Imprime  los multiplos de 10 hasta 200

print("\033[2J\033[H")
print(" --Mulitplos de 10 a 200-- ")

n = int(input("Que multiplos quieres hasta 200?: "))
c = 0

while c< 200:
    c = c + 1
    if c % n != 0:
        continue
    print (f"{c} ", end="")