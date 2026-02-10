#p012-funcion-matematicas-equacion.py
# Evaluar la función f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x))
## Usando operador de exponenciación (**) y función pow() de math


import math as mt

print("\033[H\033[J")
print("Evaluar la expresion: f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x)) ")
x = float(input("Dame X: "))
y = float(input("Dame Y: "))

fxy = 3 * mt.pow(x,2) + mt.sqrt(mt.pow(x,2) + mt.pow(y,2) ) + mt.exp(mt.log(x))

print(f"El resultado de f({x},{y}) = {fxy:.2f}")