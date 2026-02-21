# Determinar el precio de una entrada segun la edad del cliente para el cine
print("\033[2J\033[H")

print("Taquilla Cine")
edad = int(input("Ingrese su edad: "))

if edad < 5:
    print("Entrada gratis")
elif edad <= 12:
    print("El precio de la entrada es $50")
elif edad <= 17:
    print("El precio de la entrada es $70")
elif edad <= 59:
    print("El precio de la entrada es $100")
else:
    print("El precio de la entrada es $60 (descuento para adultos mayores)")

print("\nPrograma terminado")