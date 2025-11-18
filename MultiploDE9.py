n = int(input("Ingrese el valor de N: "))
m = int(input("Ingrese el valor de M: "))
for i in range(n, m + 1):
    print(i)
    if i % 9  == 0:
        print("El numero es divisible por 9")
        break
    else:
        print("El numero no es divisible por 9")