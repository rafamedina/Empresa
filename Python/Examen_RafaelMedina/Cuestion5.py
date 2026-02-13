
usuario_correcto = "admin"
clave_correcta = "1234"
intentos = 0

while intentos < 3:
    user = input("Introduce usuario: ")
    pwd = input("Introduce contraseña: ")

    if user == usuario_correcto and pwd == clave_correcta:
        print("Bienvenido, acceso concedido.")
        break
    else:
        intentos += 1
        print("Datos incorrectos.")

if intentos == 3:
    print("Acceso bloqueado por seguridad.")