n = int(input("Ingrese el valor de N (entero >= 1): "))
while n > 0:
    print(n)
    n -= 1
    if n % 7 == 0:
        print("¡Alerta! Hemos llegado a un múltiplo de 7.")
        break
print("Cuenta regresiva finalizada.")