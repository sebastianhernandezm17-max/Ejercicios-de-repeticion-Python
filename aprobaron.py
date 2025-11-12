cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: ")) 

contadorEstudiantes = 0
aprobaron = 0
reprobaron = 0
sumaDefinitiva = 0

while contadorEstudiantes < cantidadEstudiantes:
  codigoEstudiante = str(input("Ingrese el codigo del estudiante: "))
  notaDefinitiva = float(input("Ingrese la nota definitiva del estudiante: "))
  if notaDefinitiva >= 3.0:
    aprobaron += 1
  else :
    reprobaron += 1
  sumaDefinitiva = sumaDefinitiva+notaDefinitiva
  contadorEstudiantes = contadorEstudiantes+1

promedioGrupo = sumaDefinitiva/cantidadEstudiantes
print("La cantidad de estudiantes que aprobaron es: ", aprobaron)
print("La cantidad de estudiantes que reprobaron es: ", reprobaron)
print("El promedio del grupo es: ", promedioGrupo)