#p009-promedio-de-calificaciones.py
# Calcula el promedio de tres calificaciones ingresados por el usuario


#Entrada
print("Dame 3 calificaciones separadas por espacio")
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3, =int(cal1), int(cal2), int(cal3)

#Calcular promedio
suma = cal1 + cal2 +cal3 
promedio = suma / 3

#Mostrar resultado
print(f"Las calificaciones fueron   : {cal1} {cal2} {cal3}")
print(f"La suma de las calificaciones es   : {suma}")
print(f"El promedio de las calif fue  : {promedio}")
