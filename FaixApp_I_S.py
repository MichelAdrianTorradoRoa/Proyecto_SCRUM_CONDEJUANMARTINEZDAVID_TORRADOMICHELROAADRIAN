import json
import os
from secundary_funciones import *

def cargar_datos_login(archivo):
    datos_login = {}
    with open(archivo,"r") as file:
        datos_login=json.load(file)
    return datos_login

def guardar_datos_login(archivo, datos_login):
    datos_login = dict(datos_login)
    
    diccionario=json.dumps(datos_login, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
# def cargar_datos_login(archivo):
#     try:
#         with open(archivo, "r") as file:
#             datos_login = json.load(file)
#     except FileNotFoundError:
#         datos_login = {"D_Artista": [], "D_Discografica": []}
#     except json.JSONDecodeError as e:
#         print(f"Error de decodificación JSON en el archivo '{archivo}': {e}")
#         datos_login = {"D_Artista": [], "D_Discografica": []}
#     return datos_login

# def guardar_datos_login(archivo, datos_login):
#     # Crear directorio si no existe
#     directorio = os.path.dirname(archivo)
#     if not os.path.exists(directorio):
#         os.makedirs(directorio)
    
#     with open(archivo, "w") as file:
#         json.dump(datos_login, file, indent=4)

def pedir_Opc():
    while True:
        try:
            Opc = int(input("Seleccione una opción:\n👉    "))
            return Opc
        except ValueError:
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")
            print("Error de opción")
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/")

def Sign_Up_FaixApp_Artist(datos_login):
    Datos_login_Artista = {}
    print("Bienvenido Usuario")
    Datos_login_Artista["Correo"] = input("Ingrese su Correo Electronico: ")
    while True:
        Datos_login_Artista["Contrasena"] = input("Cree una contrasena: ")
        contrasena_verificar = input("Verificar contrasena: ")
        if contrasena_verificar == Datos_login_Artista["Contrasena"]:
            datos_login.setdefault("D_Artista", []).append(Datos_login_Artista)
            print("")
            print("Usuario Creado Exitosamente")
            print("")
            return
        else:
            print("Las contrasenas no coinciden")

def Sign_Up_FaixApp_Artist_(datos_login: dict):
    D_Artistas = {}
    print("Bienvenido Usuario")
    D_Artistas["Correo"] = input("Ingrese el Correo: ")
    while True:
        D_Artistas["Contrasena"] = input("Cree una contrasena: ")
        contrasena_Ver = input("Verificar Contrasena: ")
        if D_Artistas["Contrasena"] == contrasena_Ver:
            datos_login["D_Artistas"].append(D_Artistas)
            print("")
            print("Usuario Creado Exitosamente")
            print("")
            return datos_login
        else:
            print("Las Contrasenas no coinciden")
            return datos_login
            
def Sign_Up_FaixApp_Artist():
    datos_login = cargar_datos_login(BASE_DE_DATOS)
    datos_login = Sign_Up_FaixApp_Artist_(datos_login)
    guardar_datos_login(BASE_DE_DATOS, datos_login)

def Sign_Up_FaixApp_Record_Company_(datos_login: dict):
    D_Artistas = {}
    print("Bienvenido Usuario")
    D_Artistas["Correo"] = input("Ingrese el Correo: ")
    while True:
        D_Artistas["Contrasena"] = input("Cree una contrasena: ")
        contrasena_Ver = input("Verificar Contrasena: ")
        if D_Artistas["Contrasena"] == contrasena_Ver:
            datos_login["D_Artistas"].append(D_Artistas)
            print("")
            print("Usuario Creado Exitosamente")
            print("")
            return datos_login
        else:
            print("Las Contrasenas no coinciden")
            return datos_login
            
def Sign_Up_FaixApp_Record_Company():
    while True:
        datos_login = cargar_datos_login(BASE_DE_DATOS)
        datos_login = Sign_Up_FaixApp_Record_Company_(datos_login)
        guardar_datos_login(BASE_DE_DATOS, datos_login)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
def Log_In_FaixApp_Artists_(datos_login: dict):
    
    print("Bienvenido usuario")
    Correo = input("Ingrese su Correo: ")
    Contrasena_R = input("Ingrese su Contrasena: ")
    for i in range(len(datos_login["D_Artistas"])):
        if datos_login["D_Artistas"][i]["Correo"] == Correo:
            while datos_login["D_Artistas"][i]["Contrasena"] != Contrasena_R:
                print("Contrasena Incorrecta")
                Contrasena_R = input("Ingrese su Contrasena: ")
            else:
                print ("")
                print("Inicio de sesión exitoso")
                print ("")
                return datos_login
    print ("")
    print("El Usuario no esta registrado")
    print ("")
    return datos_login
            
def Log_In_FaixApp_Artists():
    datos_login = cargar_datos_login(BASE_DE_DATOS)
    datos_login = Log_In_FaixApp_Artists_(datos_login)
    guardar_datos_login(BASE_DE_DATOS, datos_login)

# def Log_In_FaixApp_Artists(datos_login):
#     print("Bienvenido usuario")
#     Correo = input("Ingrese su Correo: ")
#     Contrasena_R = input("Ingrese su Contrasena: ")
#     for Datos_login_Artista in datos_login.get("D_Artista", []):
#         if Datos_login_Artista.get("Correo") == Correo:
#             while Datos_login_Artista.get("Contrasena") != Contrasena_R:
#                 print("Contrasena Incorrecta")
#                 Contrasena_R = input("Ingrese su Contrasena: ")
#             else:
#                 print ("")
#                 print("Inicio de sesión exitoso")
#                 print ("")
#                 return
#     print ("")
#     print("El artista no esta registrado")
#     print ("")
#     return

# def Log_In_FaixApp_Record_Company(datos_login):
#     print("Bienvenido Usuario")
#     Correo = input("Ingrese su Correo: ")
#     ContrasenaR_R = input("Ingrese su Contrasena: ")
#     for Datos_login_Discografica in datos_login.get("D_Discografica", []):
#         if Datos_login_Discografica.get("Correo") == Correo:
#             while Datos_login_Discografica.get("Contrasena") != ContrasenaR_R:
#                 print("Contrasena Incorrecta")
#                 ContrasenaR_R = input("Ingrese su Contrasena: ")
#             else:
#                 print("Inicio de sesión exitoso")
#                 return
#     print("La Compañia Discografica no esta registrada")

# Código principal
BASE_DE_DATOS = "JSONfiles/data/login.json"
datos_login = cargar_datos_login(BASE_DE_DATOS)

