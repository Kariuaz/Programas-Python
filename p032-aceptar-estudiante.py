#p031-2da-ley-de-newton.py
#Calcula la fuerza, masa o aceleracion segun la ley de newton

print("\033[2J\033[H")
print ("--Calculadora de la segunda Ley de Newton")
print(" [F] uerza - f = m * a")
print(" [M] asa - m = f / a")
print(" [A] celeracion - a = m * f")
op = input("Opcion ? ").upper()

if op =="F":
    print( "\nCalculando la fuerza..")
    m = float(input("Masa   ?"))
    a = float(input("Aceleracion   ?"))
    f = m * a
    print( f"La fuerza es : {f:.2f}")
elif op =="M":
    print( "\nCalculando la Masa..")
    f = float(input("Fuerza   ?"))
    a = float(input("Aceleracion   ?"))
    m = f / a
    print( f"La fuerza es : {m:.2f}")
elif op =="A":
    print( "\nCalculando la Aceleracion..")
    m = float(input("Masa   ?"))
    f = float(input("Fuerza   ?"))
    a = f * m
    print( f"La fuerza es : {a:.2f}")