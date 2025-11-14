cantidadNumeros = int(input("Ingrese la cantidad de números: "))
        
if cantidadNumeros > 0:
    print("Tabla de Valores")
    for numero in range(1, cantidadNumeros + 1):
      print(numero, numero * numero, numero + numero * numero)
else:
    print("La cantidad no puede ser negativa. Intente de nuevo.")

