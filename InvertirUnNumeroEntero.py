n = int(input("Ingrese el valor de N: "))
r = 0
while n > 0:
    digito = n % 10 
    r = r*10 + digito 
    n //= 10
print("Número invertido:", r)