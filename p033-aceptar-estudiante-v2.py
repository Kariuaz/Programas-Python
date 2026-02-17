#Controla el acceso a la uni en base a dos condiciones
print("\033[2J\033[H")
print(" --Proceso de Ingreso a la Universidad del Bajio-- ")

nombre = input("Dame tu nombre")
edad = int(input("Edad"))

if edad < 18:
    print("Lo sentimos {nombre} solo permitimos mayores a 18")
else:
    print("Ingresa 2 calificacoines separadas por enter")
    cal1 = float(input())
    cal2 = float(input())
    if cal1 <8 or cal2 < 8:
        print("Lo sentimos {nombre}, se requieren claif mayores a 8")
    else:
        print(f"{nombre} Bienvenido a la universidad, tu edad y cali lo permiten")

print ("\nProceso terminado, gracias por participar")