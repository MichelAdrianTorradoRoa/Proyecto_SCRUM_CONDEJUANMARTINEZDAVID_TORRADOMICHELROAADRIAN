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
m_1_1 = "main/txt/main_plantillas/artistas/1-1.txt"
m_1_1_1 = "main/txt/main_plantillas/artistas/1-1-1.txt"
m_1_1_2 = "main/txt/main_plantillas/artistas/1-1-2.txt"
m_1_1_3 = "main/txt/main_plantillas/artistas/1-1-3.txt"
m_1_1_4 = "main/txt/main_plantillas/artistas/1-1-4.txt"
m_info = "main/txt/main_plantillas/artistas/info.txt"
m_info_leer = "main/txt/main_plantillas/artistas/info_leer.txt"

#Menu DISCOGRAFIA
m_1_2 = "main/txt/main_plantillas/discografia/1-2.txt"
m_1_2_1 = "main/txt/main_plantillas/discografia/1-2-1.txt"
m_1_2_2 = "main/txt/main_plantillas/discografia/1-2-2.txt"
m_1_2_3 = "main/txt/main_plantillas/discografia/1-2-3.txt"

#Login 
m_login_a = "main/txt/main_plantillas/login/login_artistas.txt"
m_login_d = "main/txt/main_plantillas/login/login_discografica.txt"