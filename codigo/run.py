"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática:
"""

def crearFacebook():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en "\
    "Facebook\nIngresar el nombre de Usuario: ")
    edadUsuario = int(input("Ingresar la edad del Usuario: "))
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    paisUsuario = input("Ingresar el país donde se ubica el Usuario: ")
    correoUsuario = ("Ingresar correo del Usuario: ")
    cadena = f"Creando cuenta de Facebook\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Edad del usuario: {edadUsuario}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"País del usuario: {paisUsuario}\n"\
    f"Correo del usuario: {correoUsuario}\n"
    return cadena

def crearTwitter():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Twitter"\
    "\nIngresar el nombre de Usuario: ")
    nombres = input("Ingresar los nombres completos del Usuario: ")
    apellidos = input("Ingresar los apellidos completos del Usuario: ")
    edadUsuario = int(input("Ingresar la edad del Usuario: "))
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    paisUsuario = input("Ingresar el país donde se ubica el Usuario: ")
    idiomaUsuario = input("Ingresar el idioma que habla el Usuario: ")
    correoUsuario = ("Ingresar correo del Usuario: ")
    print(f"Resumen de cuenta creada en Twitter\n"\
    f"Nombre del Usuario: {nombreUsuario}\n"\
    f"Nombres completos del Usuario: {nombres}\n"
    f"Apellidos completos de usuario: {apellidos}\n"\
    f"Edad del usuario: {edadUsuario}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"País del usuario: {paisUsuario}\n"\
    f"Idioma del usuario: {idiomaUsuario}\n"\
    f"Correo del usuario: {correoUsuario}\n")

def crearWhatsapp():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Whatsapp"\
    "\nIngresar el nombre de Usuario: ")
    numeroTelefono = input("Ingresar el número de teléfono del Usuario: ")
    edadUsuario = int(input("Ingresar la edad del Usuario: "))
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    paisUsuario = input("Ingresar el país donde se ubica el Usuario: ")
    cadena = f"Resumen de cuenta creada en Whatsapp\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Número del teléfono del usuario: {numeroTelefono}\n"\
    f"Edad del usuario: {edadUsuario}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"País del usuario: {paisUsuario}\n"
    return cadena

def crearTelegram():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Telegram"\
    "\nIngresar el nombre de Usuario: ")
    numeroTelefono = input("Ingresar el número de teléfono del Usuario: ")
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    paisUsuario = input("Ingresar el país donde se ubica el Usuario: ")
    areaInteres = input("Ingresar el área de interés del Usuario: ")
    print(f"Resumen de cuenta creada en Telegram\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Número del teléfono del usuario: {numeroTelefono}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"País del usuario: {paisUsuario}\n"\
    f"Área de interés del usuario: {areaInteres}\n")

def crearSignal():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Signal\n"\
    "Ingresar el nombre de Usuario: ")
    numeroTelefono = input("Ingresar el número de teléfono del Usuario: ")
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    paisUsuario = input("Ingresar el país donde se ubica el Usuario: ")
    hobbyPri = input("Ingresar el hobby principal: ")
    cadena = f"Resumen de cuenta creada en Signal\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Número del teléfono del usuario: {numeroTelefono}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"País del usuario: {paisUsuario}\n"\
    f"Hobby principal del usuario: {hobbyPri}\n"
    return cadena

def crearInstagram():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Instagram"\
    f"\nIngresar el nombre de Usuario: ")
    ciudadUsuario = input("Ingresar la ciudad donde se ubica el Usuario: ")
    edadUsuario = int(input("Ingresar la edad del Usuario: "))
    correoUsuario = ("Ingresar correo del Usuario: ")
    print("Resumen de cuenta creada en Instagram\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Ciudad del usuario: {ciudadUsuario}\n"\
    f"Edad del usuario: {edadUsuario}\n"\
    f"Correo del usuario: {correoUsuario}\n")

def crearFlickr():
    """
        explicación de método
    """
    nombreUsuario = input("Usted escogió la opción crear cuenta en Flickr\n"\
    "Ingresar el nombre de Usuario: ")
    correoUsuario = ("Ingresar correo del Usuario: ")
    cadena = f"Resumen de cuenta creada en Flickr\n"\
    f"Nombre del usuario: {nombreUsuario}\n"\
    f"Correo del usuario: {correoUsuario}\n"
    return cadena

def obtenerMensaje(cont):
    mensajeFinal = ["Campaña con poca afluencia",
    "Campaña moderada siga adelante", "Excelente campaña"]
    if ((cont >= 1) and (cont <=5)):
        cadenaFinal = mensajeFinal[0]
    elif ((cont >= 6) and (cont <= 15)):
        cadenaFinal = mensajeFinal[1]
    else:
        if ((cont >= 16)):
            cadenaFinal = mensajeFinal[2]

def principal():
    bandera = True
    contadorCuentas = 0
    while (bandera):
        opcion1 = int(input("Igresar 1 para crear una cuenta en Facebook\n"\
        f"Ingresar 2 para crear una cuenta de Twitter\n"\
        f"Ingresar 3 para crear una cuenta en Whatsapp\n"\
        f"Ingresar 4 para crear una cuenta en Telegram\n"\
        f"Ingresar 5 para crear una cuenta en Signal\n"\
        f"Ingresar 6 para crear una cuenta en Instagram\n"\
        f"Ingresar 7 para crear una cuenta en Flickr: "))
        if (opcion1 == 1):
            print(crearFacebook())
        elif (opcion1 == 2):
            crearTwitter()
        elif (opcion1 == 3):
            print(crearWhatsapp())
        elif (opcion1 == 4):
            crearTelegram()
        elif (opcion1 == 5):
            print(crearSignal())
        elif (opcion1 == 6):
            crearInstagram()
        elif (opcion1 == 7):
            print(crearFlickr())
        else :
            print("Opción incorrecta.")
        opcion2 = input("Escriba SI para crear mas cuentas\n"\
        "Escriba NO para ya no crear mas cuentas: ")
        opcion2 = opcion2.lower()
        if (opcion2 == "no"):
            bandera = False
            print(obtenerMensaje(contadorCuentas))
        else:
            if (opcion2 == "si"):
                contadorCuentas = contadorCuentas + 1
            else:
                print("Opcion incorrecta.")

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__":
    principal()
