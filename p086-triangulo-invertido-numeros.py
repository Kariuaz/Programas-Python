# p086-triangulo-invertido-numeros.py
# Imprimir un triángulo numérico invertido

limite = int(input("Dame un número: "))

for fila in range(limite, 0, -1):
    for numero in range(1, fila + 1):
        print(numero, end=" ")
    print()

print("\nPrograma terminado")