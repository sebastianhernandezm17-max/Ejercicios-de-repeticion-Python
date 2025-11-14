n = int(input("Ingrese el valor de N: "))
if n <= 0:
    print("N debe ser un número positivo.")
else:
    a = 0
    b = 1
    while a <= n:
        print(a)
        a,b = b, a + b