import json
import os

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {"D_Artista": [], "D_Discografica": []}
    except json.JSONDecodeError as e:
        print(f"Error de decodificación JSON en el archivo '{archivo}': {e}")
        datos = {"D_Artista": [], "D_Discografica": []}
    return datos

def guardar_datos(archivo, datos):
    # Crear directorio si no existe
    directorio = os.path.dirname(archivo)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

def pedir_Opc():
    while True:
        try:
            Opc = int(input("Ingrese la opción: "))
            return Opc
        except ValueError:
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")
            print("Error de opción")
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")

def Sign_Up_FaixApp_Artist(datos):
    Datos_Artista = {}
    print("Bienvenido Usuario")
    Datos_Artista["Correo"] = input("Ingrese su Correo Electronico: ")
    while True:
        Datos_Artista["Contrasena"] = input("Cree una contrasena: ")
        contrasena_verificar = input("Verificar contrasena: ")
        if contrasena_verificar == Datos_Artista["Contrasena"]:
            datos.setdefault("D_Artista", []).append(Datos_Artista)
            print("Usuario Creado Exitosamente")
            return
        else:
            print("Las contrasenas no coinciden")

def Sign_Up_FaixApp_Record_Company(datos):
    Datos_Discografica = {}
    print("Bienvenido Usuario")
    Datos_Discografica["Correo"] = input("Ingrese el Correo: ")
    while True:
        Datos_Discografica["Contrasena"] = input("Cree una contrasena: ")
        contrasena_Ver = input("Verificar Contrasena: ")
        if Datos_Discografica["Contrasena"] == contrasena_Ver:
            datos.setdefault("D_Discografica", []).append(Datos_Discografica)
            print("Usuario Creado Exitosamente")
            return
        else:
            print("Las Contrasenas no coinciden")

def Log_In_FaixApp_Artists(datos):
    print("Bienvenido usuario")
    Correo = input("Ingrese su Correo: ")
    Contrasena_R = input("Ingrese su Contrasena: ")
    for Datos_Artista in datos.get("D_Artista", []):
        if Datos_Artista.get("Correo") == Correo:
            while Datos_Artista.get("Contrasena") != Contrasena_R:
                print("Contrasena Incorrecta")
                Contrasena_R = input("Ingrese su Contrasena: ")
            else:
                print("Inicio de sesión exitoso")
                return
    print("El artista no esta registrado")

def Log_In_FaixApp_Record_Company(datos):
    print("Bienvenido Usuario")
    Correo = input("Ingrese su Correo: ")
    ContrasenaR_R = input("Ingrese su Contrasena: ")
    for Datos_Discografica in datos.get("D_Discografica", []):
        if Datos_Discografica.get("Correo") == Correo:
            while Datos_Discografica.get("Contrasena") != ContrasenaR_R:
                print("Contrasena Incorrecta")
                ContrasenaR_R = input("Ingrese su Contrasena: ")
            else:
                print("Inicio de sesión exitoso")
                return
    print("La Compañia Discografica no esta registrada")

# Código principal
BASE_DE_DATOS = os.path.join("data", "login.json")
datos = cargar_datos(BASE_DE_DATOS)

print("Bienvenido Usuario")
print("Que quieres hacer")
print("1. para Registrarse")
print("2. para Iniciar Sesion")
print("3. para salir")

while True:
    Opc = pedir_Opc()
    if Opc == 1:
        print("Como vas a Registrarte")
        print("1. Como Artista")
        print("2. Como Discografica")
        print("3. para salir")
        Op = pedir_Opc()
        if Op == 1:
            Sign_Up_FaixApp_Artist(datos)
        elif Op == 2:
            Sign_Up_FaixApp_Record_Company(datos)
        elif Op == 3:
            print("Salida Exitosa")
            break
        else:
            print("Opcion Invalida")
        guardar_datos(BASE_DE_DATOS, datos)
    elif Opc == 2:
        print("Como vas a Iniciar Sesion")
        print("1. Como Artista")
        print("2. Como Discografica")
        print("3. para salir")
        Op = pedir_Opc()
        if Op == 1:
            Log_In_FaixApp_Artists(datos)
        elif Op == 2:
            Log_In_FaixApp_Record_Company(datos)
        elif Op == 3:
            print("Salida exitosa")
            break
        else:
            print("Opcion Invalida")
    elif Opc == 3:
        print("Salida Exitosa")
        break
    else:
        print("Opcion Invalida")
