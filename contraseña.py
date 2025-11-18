contraseña = 1234
intentos = 0
contraseña = int(input("Ingrese la contraseña: "))
if contraseña == 1234:
    print("Contraseña correcta. Acceso concedido.")
while contraseña != 1234:
    print("Contraseña incorrecta. Intente de nuevo.")
    intentos += 1
    contraseña = int(input("Ingrese la contraseña: "))
    if contraseña == 1234:
        print("Contraseña correcta. Acceso concedido.")
        break
    if intentos == 2:
            print("Ha alcanzado el número máximo de intentos.")
            break
