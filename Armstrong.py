num = float(input("Ingrese el valor del numero: ")) 
suma = 0
x = num
while x > 0:
    digito = x % 10
    suma = suma + digito**3
    x = x // 10
while True:
    if num == suma:
        print("El numero es un numero de Armstrong")
    else:
        print("El numero no es un numero de Armstrong")
