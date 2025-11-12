cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: ")) 
android = 0
ios = 0
cantidadVotos = 0

while cantidadEstudiantes > cantidadVotos:
    voto = str(input("Ingrese su voto (android/ios): ")).strip().lower()
    if voto == "android":
        android = android + 1
        cantidadVotos = cantidadVotos + 1
    elif voto == "ios":
        ios = ios + 1
        cantidadVotos = cantidadVotos + 1

print("Resultados de la votacion, son Android:", android, " IOS:", ios) 
if android > ios:
    print("El sistema operativo ganador es Android")
elif ios > android:
    print("El sistema operativo ganador es IOS")
else:
    print("Hubo un empate entre Android e IOS")
