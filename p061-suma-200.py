# p061-suma-200.py
# Lee numeros y los suma hasta que el total acumulado sea mayor o igual a 200

while True:
    suma = 0
    conteo = 0

    while suma < 200:
        print(f"Suma actual: {suma}. ", end="")
        numero = int(input("Introduce un numero: "))
        suma += numero
        conteo += 1

    print("---")
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de numeros introducidos: {conteo}")

    if input("\n¿Desea continuar (S/N)? ").upper() == 'N':
        break

print("Programa Terminado.")