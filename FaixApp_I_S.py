def Sign_Up_FaixApp_Artist(datos):
    Datos_Artista = {}

    print("Bienvenido Usuario")
    Datos_Artista["Correo"] = input("Ingrese su Correo Electronico: ")

    while True:
        Datos_Artista["Contrasena"] = input("Cree una contrasena: ")
        contrasena_verificar = input("Verificar contrasena: ")
        if contrasena_verificar == Datos_Artista["Contrasena"]:
            datos["D_Artista"].append(Datos_Artista)
            print("Usuario Creado Exitosamente")
            return Datos_Artista
        else:
            print("Contrasena Incorrecta")
            print("Las contrasenas no coinciden")

def Sign_Up_FaixApp_record_company(datos):

    Datos_Discografica = {}
    
    print("Bienvenido Usuario")
    Datos_Discografica["Correo"] = input("Ingrese el Correo: ")

    while True:
        Datos_Discografica["Contrasena"] = input("Cree una contrasena: ")
        contrasena_Ver = input("Verificar Contrasena: ")
        if Datos_Discografica["Contrasena"] == contrasena_Ver:
            datos["D_Discografica"].append(Datos_Discografica)
            print("Usuario Creado Exitosamente")
            return Datos_Discografica
        else:
            print("Las Contrasenas no coinciden")

def Log_In_FaixApp_Artists(datos):
    
    print("Bienvenido usuario")
    Correo = input("Ingrese su Correo: ")
    Contrasena_R = input("Ingrese su Contrasena: ")
    
    for Datos_Artistas in datos["D_Artistas"]:
        if Datos_Artistas["Correo"] == Correo:
            while Datos_Artistas["Contrasena"] != Contrasena_R:
                print("Contrasena Incorrecta")
                Contrasena_R = input("Ingrese su Contrasena: ")
            else:
                return
            
    print("El artista no esta registrado")
    return


def Log_In_FaixApp_Record_Company(datos):

    print("Bienvenido Usuario")
    Correo = input("Ingrese su Correo: ")
    ContrasenaR_R = input("Ingrese su Contasena: ")

    for Datos_Discografica in datos["D_Discografica"]:
        if Datos_Discografica["Correo"] == Correo:
            while Datos_Discografica["Contrasena"] != ContrasenaR_R:
                print("Contrasena Incorrecta")
                ContrasenaR_R = input("Ingrese su Contrasena: ")
            else:
                return
            
        
    print(E)
