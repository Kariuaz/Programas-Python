#Clasifica un tiangulo segun  la long de sus lados

print("\033[2J\033[H")
print(" --Clsificador de Triangulos-- ")

L1 = float(input("Lado 1: "))
L2 = float(input("Lado 2: "))
L3 = float(input("Lado 3: "))

if L1 == L2 == L3 :
    print ("Equilatero")
if L1 == L2 or L1 == L3 or L2 == L3:
    print ("Isoceles")
else:
    print("Escaleno")

print("\nAdios, gracias por utilizar el programa")