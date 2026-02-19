#Suma numeros hasta un total de 5000, pero cuenta hasta 200

print("\033[2J\033[H")
print(" --Cuantos boletos tengo que hacer para juntar 5000-- ")

n = int(input("Cuanto quieres recaudar? "))

b = 0 
d = 0

while b < 200:
    b = b + 1
    d = d + b
    print(b, end= " ")

    if d >= n:
        print("Ya tengo el dinero necesario")
        break


if d < n:
    print(f"200 boletos no te alcanza para llegar a {n}")
else:
    print(f"Use {b} boletos para llegar a $ {d}")

