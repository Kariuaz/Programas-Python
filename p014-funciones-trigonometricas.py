#p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas básicas



import math as mt

print("\033[H\033[J")
print("DEMOSTRANDO EL USO DE FUNCIONES TRIGONOMETRICAS")

angulo = 45 # grados
radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tang = mt.tan(radianes)

grados = mt.degrees(radianes) # a grados

salida = ( "Resumen de funciones \n"
f"Seno  :  {seno:.4f} \n"          
f"Coseno  :  {coseno:.4f} \n"
f"Tangente  :  {tang:.4f} \n"      
f"El angulo {angulo:.4f} grados, en radianes equivale a {grados:.1f}\n"
f"El angulo {angulo:.4f} radianes, en grados equivale a {radianes:.4f}\n")

print(salida)