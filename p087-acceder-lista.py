# p087-acceder-lista.py
# Accede a elementos de una lista

mediciones = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\033[H\033[J')

print('Acceder a los elementos de una lista\n')

print('\nLongitud y contenido de las mediciones:')
print(f'Cantidad de mediciones : {len(mediciones)}')
print(f'Todas las mediciones   : {mediciones}')

print('\nPrimera y última medición, por índice positivo:')
print(f'Primera  : {mediciones[0]}')
print(f'Última   : {mediciones[8]}')

print('\nPrimera y última medición, por índice negativo:')
print(f'Primera  : {mediciones[-9]}')
print(f'Última   : {mediciones[-1]}')

print('\nPor rango:')
print(f'Mediciones de la 2 a la 6 (6 no incluida): {mediciones[2:6]}')

print('\nPor saltos consecutivos:')
print(f'Las primeras 3 desde el principio : {mediciones[:3]}')
print(f'Las últimas 3 desde el índice 6   : {mediciones[6:]}')

print("\nPrograma terminado")