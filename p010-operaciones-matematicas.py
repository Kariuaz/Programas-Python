#p010-operaciones-matematicas.py 
#Demuestra el uso de diferentes operadores aritmeticos

print("\033[H\033[J") #IMPRIME UNA SECUENCIA ANSI QUE BORRA LA PANTALLA
print("=" * 50)
print ("Calculadora de operaciones matematicas")
print("=" * 50)

X = float(input("Dame el valor de X : ")) 
Y = float(input("Dame el valor de Y : ")) 

print(f"Los valores de X y Y son: {X} {Y}")
print("-" * 40)

#Mostrar resultados de las operaciones directamente, con formato alineado
print(f"Suma   : {X:>6} + {Y:>6} = {X + Y:>10.2f}")
print(f"Resta  : {X:>6} - {Y:>6} = {X - Y:>10.2f}")
print(f"Multi  : {X:>6} * {Y:>6} = {X * Y:>10.2f}")
print(f"Div    : {X:>6} / {Y:>6} = { X / Y:>10.2f}")
print(f"Exp    : {X:>6} - {Y:>6} = {X ** Y:>10.2f}")
print(f"Modulo : {X:>6} % {Y:>6} = {X % Y:>10.2f}")
print(f"Div E  : {X:>6} // {Y:>6} = {X // Y:>10.2f}")