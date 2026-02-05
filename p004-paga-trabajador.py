#p004-paga-trabajador.py
#Calcula la paga de un trabajador

print("Calculando la paga de un trabajdor")

nombre = input("nombre > ")
horas = int(input("Horas trabajadas > "))
paga = float(input("Paga x hora > "))

tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("Resumen de pagos : \n")
print(f"El trabajador {nombre}, trabajo {horas}, con una paga de {paga} pesos, impuesto de {tasa} %")
print(f"paga bruta : {pagabruta}")
print(f"Impuesto : {impuesto}")
print(f"Paga neta : {paganeta}")