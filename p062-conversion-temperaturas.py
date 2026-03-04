# p062-conversion-temperaturas.py
# Programa que muestra la conversión a Fahrenheit para cada grado

while True:
    temp_inicial = int(input("Introduce la temperatura inicial en °C: "))
    temp_final = int(input("Introduce la temperatura final en °C: "))

    celsius = temp_inicial

    while celsius <= temp_final:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        celsius += 1

    if input("\n¿Desea continuar (S/N)? ").upper() == 'N':
        break

print("Programa Terminado.")