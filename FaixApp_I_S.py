def Sign_In_FaixApp_Artisrt(datos):
    Datos_Artista = {}

    print("Bienvenido Usuario")
    Datos_Artista["Nombre del Artista"] = input("Ingrese su nombre artistico: ")
    Datos_Artista["Contraseña"] = input("Cree una contraseña: ")

    while True:
        contraseña_verificar = input("Verificar contraseña: ")
        if contraseña_verificar == Datos_Artista["Contraseña"]:
            datos["D_Artista"].append(Datos_Artista)
            print("Usuario Creado Exitosamente")
            return Datos_Artista
        else:
            print("Contraseña Incorrecta")
            print("Las contraseñas no coinciden")

def Sign_In_FaixApp_record_company(datos):
    Datos_Discografica = {}
    
    print("Bienvenido Usuario")
    Datos_Discografica["Nombre de la Discografica"] = input("Ingrese el nombre de la discografica: ")
    Datos_Discografica["Contraseña"] = input("Cree un contraseña: ")

    while True:
        contraseña_Ver = input("Verificar Contraseña: ")
        if Datos_Discografica["Contraseña"] == contraseña_Ver:
            datos["D_Discografica"].append(Datos_Discografica)
            print("Usuario Creado Exitosamente")
            return Datos_Discografica
        else:
            print("Las Contraseñas no coinciden")
