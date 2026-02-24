    


print("\033[H\033[J")
print(" --Imprime una tabla de 1 hasta 10-- ")

t = 1
while t <= 10:
    z = 1
    print(f"\nTabla del {t}")
    while z<= 5:
        print(f"{t} x {z} = {z*t}")
        z = z + 1
    t = t +1