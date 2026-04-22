"""
Programa de gestión de vuelos
Nombre: Karina Lizeth Alfaro Hernandez
Matrícula: 35165728
Materia: Computación Aplicada
Examen: Segundo examen parcial
"""

print('\033[H\033[J')

# Lista de almacenamiento de vuelos
lista_vuelos = []

print("Ingresa los datos de los vuelos. Escriba '*' para terminar.\n")

while True:
    num_vuelo = input("Número de vuelo (ej. AM-202): ")
    if num_vuelo == '*':
        break

    origen_v = input("Origen: ")
    destino_v = input("Destino: ")
    aerolinea_v = input("Aerolínea: ")

    try:
        num_pasajeros = int(input("Pasajeros: "))
    except ValueError:
        print("Error: Debe ingresar un número entero para pasajeros.")
        continue

    try:
        tarifa_v = float(input("Tarifa: "))
    except ValueError:
        print("Error: Debe ingresar un número válido para la tarifa.")
        continue

    vuelo = {
        "num_vuelo": num_vuelo,
        "origen_v": origen_v,
        "destino_v": destino_v,
        "aerolinea_v": aerolinea_v,
        "num_pasajeros": num_pasajeros,
        "tarifa_v": tarifa_v
    }

    lista_vuelos.append(vuelo)

# === Datos crudos ===
print("\n=== Datos (Lista de diccionarios) ===")
print(lista_vuelos)

# === Tabla de datos ===
print("\n=== Tabla de datos ===")
print(f"{'Vuelo':10} {'Origen':15} {'Destino':15} {'Aerolínea':15} {'Pasajeros':10} {'Tarifa':10}")
print("-" * 75)
for v in lista_vuelos:
    print(f"{v['num_vuelo']:10} {v['origen_v']:15} {v['destino_v']:15} {v['aerolinea_v']:15} {v['num_pasajeros']:10} {v['tarifa_v']:10.2f}")

# === Resumen ===
print("\n=== Resumen ===")

total_vuelos = len(lista_vuelos)
print(f"Vuelos totales: {total_vuelos}")

# Conteo por aerolínea y destino
aerolineas = {}
destinos = {}
for v in lista_vuelos:
    aerolineas[v["aerolinea_v"]] = aerolineas.get(v["aerolinea_v"], 0) + 1
    destinos[v["destino_v"]] = destinos.get(v["destino_v"], 0) + 1

print("\nAerolíneas:")
for a, c in aerolineas.items():
    print(f"- {a}: {c}")

print("\nDestinos:")
for d, c in destinos.items():
    print(f"- {d}: {c}")

# Totales y promedios
suma_pasajeros = sum(v["num_pasajeros"] for v in lista_vuelos)
prom_pasajeros = suma_pasajeros / total_vuelos
suma_tarifas = sum(v["tarifa_v"] for v in lista_vuelos)
prom_tarifas = suma_tarifas / total_vuelos

# Más caro y más barato
tarifa_max = max(v["tarifa_v"] for v in lista_vuelos)
tarifa_min = min(v["tarifa_v"] for v in lista_vuelos)
vuelo_max = next(v for v in lista_vuelos if v["tarifa_v"] == tarifa_max)
vuelo_min = next(v for v in lista_vuelos if v["tarifa_v"] == tarifa_min)

print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {prom_pasajeros:.2f}")
print(f"Tarifa -> Suma: {suma_tarifas:.2f}, Promedio: {prom_tarifas:.2f}")
print(f"\n{vuelo_max['num_vuelo']} de ${tarifa_max:.2f} es el más caro.")
print(f"{vuelo_min['num_vuelo']} de ${tarifa_min:.2f} es el más barato.")

print("\nPrograma terminado.")
