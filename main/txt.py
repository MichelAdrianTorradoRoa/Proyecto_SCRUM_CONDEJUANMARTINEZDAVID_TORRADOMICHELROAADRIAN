from secundary_funciones import fecha,os,line

def mostrar_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Se produjo un error al intentar leer el archivo: {e}")
        

principal = "main/txt/main_plantillas/principal.txt"

#Menu ARTISTAS
m_1 = "txt/main_plantillas/principal.txt"