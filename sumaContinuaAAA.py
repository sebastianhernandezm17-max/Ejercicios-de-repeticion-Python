x = 0
while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n == 0:
        break
    if n < 0:
        print("Número no válido")
        continue
    else:
     x = x +n
     print("La suma de los números ingresados es:", sum(range(x+1)))