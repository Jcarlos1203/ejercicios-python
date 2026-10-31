intentos = 0
clave = ""

while intentos < 3 and clave != "1234":
    clave = input("Contraseña: ")
    intentos= intentos + 1

if clave == "1234":
    print("contraseña correcta")
else:
    print("contraseña incorrecta, consulta a soporte")
