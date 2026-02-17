#Muestra el tipo de angulo en base a su magnitud

print("\033[2J\033[H")
print(" --Clsificador de Angulos-- ")

angulo = int(input("Dame angulo en grados ? "))

if angulo>=0 and angulo <=360:
    if angulo <90:
        print("Agudo")
    elif angulo == 90:
        print("RECTO")
    elif angulo < 180:
        print("OBTUSO")
    elif angulo == 180:
        print("LLANO")  
    elif angulo < 360:
        print("CONCAVO") 
    else:
        print("COMPLETO")  

else:
    print("Angulo fuera de rango")
