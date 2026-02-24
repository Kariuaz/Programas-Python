#p052-tabla-conversion.py


tc = 19.70

while True: 
    print("\033[H\033[J")
    print(" --Mostrar una tabla de conversoin de peso a dolar en un rango especifico-- ")
    while True:
        pi = int(input("Dame valor inicial: "))
        pf = int(input("Dame valor final: "))
        if (pi> 0 and pf>0) and pi < pf : break

    c = pi
    print(f"Peso\t\tDollar")
    print("-"*30)

    while c <= pf :
        print(f"{c:>10} - {c/tc:>10.2f}")
        c = c + 1
    print("-"*30)

    if input("Deseas continuar (S/N) ? ").upper() == "N" : break

print("\nProceso terminado")
