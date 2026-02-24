#p053-conjetura-collatz.py

while True:
    print("\033[H\033[J")
    print(" --Imprime la conjetura de Collatz-- ")

    while True:
        n = int(input("Dame numero\n"))
        if n>1: break

    p=0
    while True:
        if n==1: break
        print(n, end=" ")
        p+=1
        if n% 2 == 0:
            n = n // 2
        else: 
            n = n * 3 + 1
        
    print (n, end=" ")

    print (f"\n\nPasos hasta llegar a 1 : {p}")

    if input("\nDeseas continuar (S/N)? ").upper() == "N" : break

print("\n\nProceso Terminado...")
