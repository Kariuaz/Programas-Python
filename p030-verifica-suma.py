#p030-verifica-suma.py
#Verifica si la suma de dos numeros es igual a un tercer
# n1 n2 n3 n1 n2 n3 n1 n2 n3
#5 4 9  10 22 10 5 3 2  10 10 10  1 5 7


print ("Dame 3 num enteros separados por espacio")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1),int(n2),int(n3),

if n1 + n2 == n3:
    print(f"{n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"{n1} + {n3} = {n2}")
elif n2 + n3 == n1:
    print(f"{n2} + {n3} = {n1}")
elif n2 == n3 == n1:    
    print(f"{n2} == {n3} = {n1}")
else:
    print(f"Todos los num son diferentes : {n2}, {n3}, {n1}")

print("\nGracias por usar el programa")

