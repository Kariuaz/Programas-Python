#p005-calculadora-imc.py
#Calcular el IMC de una persona

print("Calculando e indice de masa corporal")

peso_kg = float (input("Dame tu peso en kg: "))
altura_m = float(input("Dame tu altura en metros: "))

imc = peso_kg / (altura_m** 2)

print(f"Si tienes un peso de {peso_kg} y una altura de {altura_m} tu IMC es {imc:.2F}")