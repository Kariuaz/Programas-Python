# p078-piramide-caracter.py
# Imprimir una piramide de caracteres

print('\033[H\033[J')
print('Imprime una piramide de caracteres')

n = int(input('Introduce la altura de la piramide: '))
car = input('Introduce el carácter para la piramide: ')

for i in range(1, n + 1):
    espacios = n - i
    caracteres = 2 * i - 1
    for j in range(espacios):
        print(' ', end=' ')
        for k in range(caracteres):
            print(car, end='')

print()