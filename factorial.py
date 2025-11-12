num = int(input("Ingrese el numero para el factorial: ")) 
if num < 0:
    print("No se puede calcular el factorial de un numero negativo")
else:
    factorial = 1
    inferior = 1
    while inferior <= num:
     factorial = factorial * inferior
     inferior = inferior + 1
     print("El factorial de", num, "es", factorial)