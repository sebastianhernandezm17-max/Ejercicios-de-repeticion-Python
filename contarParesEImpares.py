cantidad = int(input("Ingrese cuantos numeros desea saber si es par o impar: "))
pares = 0
impares = 0
while cantidad > 0:
    n = int(input("Ingrese el valor de N: "))
    if n % 2 == 0:
        print(f"El numero {n} es par")
        pares += 1
    else:
        print(f"El numero {n} es impar")
    cantidad -= 1
    impares += 1
print("La cantidad de numeros pares es:", pares)
print("La cantidad de numeros impares es:", impares)