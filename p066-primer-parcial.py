# p066_PrimerExamenParcial_V2.py

"""
Objetivo: [Programa que administra la venta de boletos]
Nombre del Alumno: Karina Lizeth Alfaro Hernández
Matrícula: [35165728]
Materia: Computación Aplicada
Examen: Primer Parcial
"""

print("\033[H\033[J")

# --- Contadores Generales ---
contador_ventas = 0

asist_est = 0
asist_adult = 0
asist_senior = 0
asist_acad = 0

asist_total = 0
rechazados_total = 0
hombres_total = 0
mujeres_total = 0
acum_edades = 0

# --- Acumuladores de ingresos ---
ing_est = 0.0
ing_adult = 0.0
ing_senior = 0.0
ing_acad = 0.0
ing_total = 0.0

# --- Precios ---
PRECIO_EST = 50.0
PRECIO_ADULT = 90.0
PRECIO_SENIOR = 60.0
PRECIO_ACAD = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

continuar = "s"

while continuar == "s":
    contador_ventas += 1
    print(f"\n--- Nueva Venta {contador_ventas} ---")

    edad_cliente = int(input("Introduce la edad del comprador: "))

    if edad_cliente <= 13:
        print("🛑Acceso denegado🛑: El comprador es menor de edad")
        rechazados_total += 1
        continue

    print('------------------------')
    print("\nTipo de comprador:")
    print("1 Estudiante ($50)")
    print("2 Adulto ($90)")
    print("3 Tercera Edad ($60)")
    print("4 Académico ($70)")
    tipo = input("Elige el tipo de comprador (E/A/TE/AC): ").upper()
    print('--------------------------')
    genero = input("Introduce el sexo del comprador (H/M): ").lower()
    print('--------------------------')

    if tipo == "E":
        tipo_txt = "Estudiante"
    elif tipo == "A":
        tipo_txt = "Adulto"
    elif tipo == "TE":
        tipo_txt = "Tercera edad"
    elif tipo == "AC":
        tipo_txt = "Académico"
    else:
        print("🛑Tipo de comprador no válido. Venta cancelada.🛑")
        continue

    print(f"¡Bienvenido(a)! Datos registrados: {edad_cliente} años, sexo: {'hombre' if genero=='h' else 'mujer'}, Tipo: {tipo_txt}")

    asist_total += 1
    acum_edades += edad_cliente

    if genero == "h":
        hombres_total += 1
    elif genero == "m":
        mujeres_total += 1

    # --- Cálculo del costo ---
    if tipo == "E":
        asist_est += 1
        ing_est += PRECIO_EST
        ing_total += PRECIO_EST
        print(f"El precio del boleto es: {PRECIO_EST:.2f}")

    elif tipo == "A":
        asist_adult += 1
        ing_adult += PRECIO_ADULT
        ing_total += PRECIO_ADULT
        print(f"El precio del boleto es: {PRECIO_ADULT:.2f}")

    elif tipo == "TE":
        asist_senior += 1
        ing_senior += PRECIO_SENIOR
        ing_total += PRECIO_SENIOR
        print(f"El precio del boleto es: {PRECIO_SENIOR:.2f}")

    elif tipo == "AC":
        asist_acad += 1
        ing_acad += PRECIO_ACAD
        ing_total += PRECIO_ACAD
        print(f"El precio del boleto es: {PRECIO_ACAD:.2f}")

    continuar = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- Promedio ---
prom_edad = acum_edades / asist_total if asist_total > 0 else 0

# --- Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
print(f"Total Estudiantes: {asist_est}")
print(f"Total Adultos: {asist_adult}")
print(f"Total Tercera Edad: {asist_senior}")
print(f"Total Académicos: {asist_acad}")
print('----------------------------------')
print(f"Total Hombres: {hombres_total}")
print(f"Total Mujeres: {mujeres_total}")
print('----------------------------------')
print(f"Total Asistentes: {asist_total}")
print(f"Promedio de edad: {prom_edad:.2f}")
print(f"Total Rechazados (menores de 13 años): {rechazados_total}")

print("\n--- 💲Reporte de Ingresos💲 ---")
print(f"Ingresos Estudiantes: ${ing_est:.2f}")
print(f"Ingresos Adultos: ${ing_adult:.2f}")
print(f"Ingresos Tercera Edad: ${ing_senior:.2f}")
print(f"Ingresos Académicos: ${ing_acad:.2f}")
print('----------------------------------')
print(f" INGRESOS TOTALES: ${ing_total:.2f}")

print("\n--- Rentabilidad ---")
if ing_total < 1500:
    print("La función generó ganancias bajas.")
elif ing_total <= 3500:
    print("La función generó ganancias moderadas.")
else:
    print("La función generó ganancias buenas.")

print("\nProceso terminado.✔")

"""
Preguntas: Explica con tus palabras

 Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

Seria necesario preguntarle qué día es, por ejemplo: “¿Qué día es hoy?” 
Y la pregunta debe ir antes de calcular el precio del boleto, porque ahí es donde se decide cuánto va a pagar la persona, 
antes de cuando el comprador ya eligió su tipo (E, A, TE, AC) y antes de que el programa sume el precio del boleto
Cuando el comprador sea Adulto, el programa debe revisar si el día es martes.
Si sí lo es, entonces el precio del adulto se reduce un 20%.


2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

Primero me fijaría en cada parte donde se cobra un boleto, las líneas donde se suma al total general y la línea 
donde se imprime el total recaudado en el reporte final.
Si en uno de ellos solo sumas al tipo por ejemplo, solo a estudiantes, pero no al total general, ahí estaría el error.

Tambien se pudiera revisar si en alguna parte se está restando al total general por error o se está reiniciando
 el total a cero sin querer o algo que cambie el valor del total cuando ya debería estar sumando.

Haría una prueba sencilla, por ejemplo:
- 1 estudiante
- 1 adulto
Si el dinero por tipo está bien, pero el total no, eso confirma que el problema está en:
Cómo se está sumando el total general o en qué variable se está usando al final.
"""