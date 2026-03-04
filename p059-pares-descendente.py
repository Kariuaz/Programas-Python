# p059-pares-descendente.py
# Programa para numeros pares descendentes desde 100 hasta n y su suma total

while True:
    n = int(input("Introduce un numero límite (menor o igual a 100): "))

    i = 100
    suma = 0
    contador = 0
    print("Numeros pares:", end=" ")

    while i >= n:
        if i % 2 == 0:
            if contador == 0:
                print(i, end="")
            else:
                print(", " + str(i), end="")
            suma += i
            contador += 1
        i -= 1

    print("\nLa suma de los pares es:", suma)

    if input('\n¿Deseas continuar (S/N)? ').upper() == 'N': break

print("Programa Terminado.")