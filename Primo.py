import math
n = int(input("Ingrese el valor de N: "))
es_primo = True
if n <= 1:
    print("No es primo")
    es_primo = False
elif n == 2:
    print("Es primo")
    es_primo = True
elif n % 2 == 0:
    print("No es primo")
    es_primo = False
else:
    lim = int(math.sqrt(n))
    for i in range(3, lim + 1, 2):
        if n % i == 0:
            print("No es primo")
        break           
if es_primo:
    print(n,"es primo")
else:
    print(n,"no es primo")