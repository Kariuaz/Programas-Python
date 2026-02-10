#p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios


import math as mt

print("\033[H\033[J")
print("DEMOSTRANDO EL USO DE FUNCIONES REDONDEO")


precio = 15.656
print(f"Precio: {precio}")
print(f"Arriba: {mt.ceil(precio)}")
print(f"Abaj: {mt.floor(precio)}")
print(f"Truncar: {mt.trunc(precio)}")
print(f"normal: {round(precio)}")
print(f"2 Dec: {round(precio,2)}")