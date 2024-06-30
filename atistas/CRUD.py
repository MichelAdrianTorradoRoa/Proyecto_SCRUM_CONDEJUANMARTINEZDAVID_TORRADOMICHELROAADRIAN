from datos import *
from funciones_secundarias import very,clear_screen, print_
from CRUD_funciones import contador_id
#CREAR

def crear_song(datos: dict):
    canciones={}
    canciones["nombre"]=input("Ingrese el nombre de la cancion: ").lower()
    canciones["artista"]=input("Ingrese el nombre del artista: ")
    while True:
        op = input("Ingrese el genero de la cancion: \n    1. Rock\n    2. Pop\n    3. Urbana\n    4. Electronica\n    5. Rap\n>>    ")
        if op == "1": 
            canciones["genero"] = "Rock"
            canciones["genero_id"] = "01"             
            break
        elif op == "2":
            canciones["genero"] = "Pop"
            canciones["genero_id"] = "02"  
            break
        elif op == "3":
            canciones["genero"] = "Urbana"
            canciones["genero_id"] = "03"  
            break
        elif op == "4":
            canciones["genero"] = "Electronica"
            canciones["genero_id"] = "04"                   
            break
        elif op == "5":
            canciones["genero"] = "Rap"
            canciones["genero_id"] = "05"                   
            break
        else:
            print_("El genero no es valido")
    canciones["duracion"]=input("Ingrese la duracion: ")
    canciones["lanzamiento"]=input("Ingrese el lanzamiento de la cancion: ")
    canciones["album"]=input("Ingrese el nombre del album: ")
    canciones["artista_id"]= contador_id()
    
    datos["canciones"].append(canciones)
    print(canciones["nombre"]," registrado con éxito!")
    return datos

def crear_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = crear_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
crear_cancion()

#ELIMINAR
def eliminar_song(datos: dict):
    nombre =input("Ingrese el nombre de la cancion: ").lower()
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["nombre"] == nombre:
            song = ("La cancion ",datos["canciones"][i]["nombre"]," de ",datos["canciones"][i]["artista"])
            datos["canciones"].pop(i)
            separador = " "
            song = separador.join(map(str, song))
            print(song,"eliminada con exito...")
            return datos
    print (f"La cancion ",nombre," no existe...")    
    return datos

def eliminar_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = eliminar_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
eliminar_cancion()
