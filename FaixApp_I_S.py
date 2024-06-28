def Sign_In_FaixApp_Artisrt(datos):
    Datos_Artista = {}

    print("Bienvenido Usuario")
    Datos_Artista["Nombre del Artista"] = input("Ingrese su nombre artistico: ")
    Datos_Artista["Contraseña"] = input("Cree una contraseña: ")

    while True:
        contraseña_verificar = input("Verificar contraseña: ")
        if contraseña_verificar == Datos_Artista["Contraseña"]:
            Datos_Artista["D_Artista"].append(Datos_Artista)
            print("Usuario Creado Exitosamente")
        else:
            print("Contraseña Incorrecta")
            print("Las contraseñas no coinciden")