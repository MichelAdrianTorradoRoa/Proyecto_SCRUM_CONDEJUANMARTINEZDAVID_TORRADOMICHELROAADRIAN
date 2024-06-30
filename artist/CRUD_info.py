from artist.datos import *
from artist.funciones_secundarias import very,clear_screen, print_, es, linen,linea,line
from artist.CRUD_funciones import contador_id
#CREAR

def crear_informacion(datos: dict):
    artistas={}
    artistas["nombre"]=input("Ingrese el nombre del artista: ").lower()
    artistas["descripcion"]=input("Ingrese una breve descripcion del artista: ").lower()
    artistas["contacto"]=input("Ingrese la info de contacto del artista: ").lower()
    
    datos["artistas"].append(artistas)
    print(artistas["nombre"]," registrado con éxito!")
    return datos

def crear_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = crear_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# crear_info()

#ELIMINAR
def eliminar_informacion(datos: dict):
    nombre =input("Ingrese el nombre del artista: ").lower()
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            informacion = (datos["artistas"][i]["nombre"])
            datos["artistas"].pop(i)
            separador = " "
            informacion = separador.join(map(str, informacion))
            print(informacion," se ha eliminado con exito...")
            return datos
    print (f"El artista ",nombre," no esta resgistrado...")    
    return datos

def eliminar_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = eliminar_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# eliminar_info()


#LEER
def leer_informacion(datos: dict):
    nombre =input("Ingrese el nombre del artista: ").lower()    
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["artistas"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("D e s c r i p c i o n")
            print_(datos["artistas"][i]["descripcion"].capitalize())
            line()
            es()
            line()
            print_("C o n t a c t o")
            print_(datos["artistas"][i]["contacto"])
            line()
            es()
            line()
            print_("C a n c i o n e s")
            for i in range(len(datos["canciones"])):
                if datos["canciones"][i]["artista"] == nombre:
                    # for sn in range(len(datos["canciones"][i]["nombre"])):
                    print_ (datos["canciones"][i]["nombre"])
            line()
            es()
            linea()
            return datos
    print_(f"El artista ",nombre," no se encuentra registrado...")    
    return datos

def leer_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# leer_info()


#ACTUALIZAR
def actualizar_informacion(datos: dict):
    nombre =input("Ingrese el nombre del artista: ").lower()    
    for i in range(len(datos["artistas"])):
        if datos["artistas"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. Descripcion\n    3. Contacto\n\n>>  ")
                if op == "1": 
                    name =  datos["artistas"][i]["nombre"]
                    datos["artistas"][i]["nombre"]=input("Ingrese el nuevo nombre del artista: ").lower()
                    es()
                    print_(f"El nombre ",name," ha sido cambiada a ", datos["artistas"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "2": 
                    descripcion =  datos["artistas"][i]["descripcion"]
                    datos["artistas"][i]["descripcion"]=input("Ingrese la nueva descripcion del artista: ").lower()
                    es()
                    print_(f"La descripcion ",descripcion," ha sido cambiada a ", datos["artistas"][i]["descripcion"]," con éxito!")
                    return datos
                elif op == "3": 
                    contacto =  datos["artistas"][i]["contacto"]
                    datos["artistas"][i]["contacto"]=input("Ingrese el nuevo contacto del artista: ").lower()
                    es()
                    print_(f"El contacto ",contacto," ha sido cambiada a ", datos["artistas"][i]["contacto"]," con éxito!")
                    return datos
                elif op == "0": return datos 
                else: print_("Opcion no valida")
    print(f"El artista ",nombre," no se encuentra registrado...")     
    return datos

def actualizar_info():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = actualizar_informacion(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# actualizar_info()

