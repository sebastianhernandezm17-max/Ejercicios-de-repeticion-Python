tablasMultiplicar = int(input("Que tabla desea practicar(1/20): "))
aciertos = 0
if 1 <= tablasMultiplicar <= 20:
    print("Tabla de multiplicar del", tablasMultiplicar)
for i in range(1, 11): 
    try:
        respuesta = int(input(f"{tablasMultiplicar} x {i} = "))
    except ValueError:
        print(f"Respuesta no válida. La respuesta correcta es {tablasMultiplicar * i}.")
        continue
    if respuesta == tablasMultiplicar * i:
        aciertos += 1
        print("Correcto. ¡Bien hecho!")
    else:
        print(f"Incorrecto. {tablasMultiplicar} x {i} = {tablasMultiplicar * i}")
        print(f"Has obtenido {aciertos} aciertos de 10.")
    puntos = aciertos *10
    print(f"Has ganado {puntos} puntos.")
    if puntos <= 50:
        print("insuficiente")
    elif puntos == 60 or puntos == 70:
            print("aceptable")
    elif puntos == 80 or puntos == 90:
            print("sobresaliente")
    elif puntos == 100:
         print("excelente")