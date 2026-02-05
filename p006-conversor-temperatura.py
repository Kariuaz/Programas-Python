# p006-conversor-temperatura.py
# Convertir temperatua de grados Celsius a Farenheit

print("Convirtiendo grados Celsius a grados Farenheit")

celcius = float(input("Ingresa la temp Celsius: "))

farenheit = (celcius * 9 / 5 ) + 32

print(f"{celcius} grados celsius equivale a {farenheit:.2f} grados farenheit")