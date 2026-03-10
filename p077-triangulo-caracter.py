# p077-triangulo-caracter.py
# Imprimir un triangulo rectangulo de caracteres

print('\033[H\033[J')
print('Imprime un triangulo rectangulo de n renglones del caracter deseado')

n = int(input('¿Cuantos renglones tendra el triangulo? '))
car = input('¿Que caracter quieres usar? ')

for i in range(1, n + 1):
    for j in range(i):
        print(car, end='')
print()