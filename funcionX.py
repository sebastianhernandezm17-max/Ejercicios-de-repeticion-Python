x = int(input("Ingrese el valor de x: "))
if x > 0:
   for x in range(0, x+1,2):
     funcion = x**3 + x**2 - 5
     print("Para x = ", x," f(x) = ",funcion)