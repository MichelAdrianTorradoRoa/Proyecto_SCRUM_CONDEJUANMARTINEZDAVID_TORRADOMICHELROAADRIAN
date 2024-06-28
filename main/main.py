from importaciones import *

while True:
    clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Seleccione una opcion:\n👉   ")
    line()
    if op == "1": 
        while True:
            mostrar_txt(m_1_1)
            op_1_1 = input("Seleccione una opcion:\n👉   ")
            line()
            if op_1_1 == "1": 
                while True:
                    mostrar_txt(m_1_1_1)
                    op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_1_1_1 == "1":
                        print ("crear_album")
                    elif op_1_1_1 == "2":
                        print ("crear_cancion")
                    elif op_1_1_1 == "3":
                        print ("crear_sencillo")
                    elif op_1_1_1 == "4":
                        mostrar_txt(m_info)
                        op_info = input("Seleccione una opcion:\n👉   ")
                        if op_info == "1":
                            print ("crear_descripcion")
                        elif op_info == "2":
                            print ("crear_info_contacto")
                        elif op_info == "3": break
                        else: print ("opcion no valida")
                    elif op_1_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_1_1 == "2": 
                while True:
                    mostrar_txt(m_1_1_2)
                    op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_1_1_1 == "1":
                        print ("eliminar_album")
                    elif op_1_1_1 == "2":
                        print ("eliminar_cancion")
                    elif op_1_1_1 == "3":
                        print ("eliminar_sencillo")
                    elif op_1_1_1 == "4":
                        mostrar_txt(m_info)
                        op_info = input("Seleccione una opcion:\n👉   ")
                        if op_info == "1":
                            print ("eliminar_descripcion")
                        elif op_info == "2":
                            print ("eliminar_info_contacto")
                        elif op_info == "3": break
                        else: print ("opcion no valida")
                    elif op_1_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_1_1 == "3":
                while True:
                    mostrar_txt(m_1_1_3)
                    op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_1_1_1 == "1":
                        print ("actualiza_album")
                    elif op_1_1_1 == "2":
                        print ("actualizar_cancion")
                    elif op_1_1_1 == "3":
                        print ("actualizar_sencillo")
                    elif op_1_1_1 == "4":
                        mostrar_txt(m_info)
                        op_info = input("Seleccione una opcion:\n👉   ")
                        if op_info == "1":
                            print ("actualizar_descripcion")
                        elif op_info == "2":
                            print ("actualizar_info_contacto")
                        elif op_info == "3": break
                        else: print ("opcion no valida")
                        print ("actualizar_info")
                    elif op_1_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_1_1 == "4": 
                while True:
                    mostrar_txt(m_1_1_4)
                    op_1_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_1_1_1 == "1":
                        print ("leer_albunes")
                    elif op_1_1_1 == "2":
                        print ("leer_canciones")
                    elif op_1_1_1 == "3":
                        print ("leer_sencillos")
                    elif op_1_1_1 == "4":
                        mostrar_txt(m_info_leer)
                        op_info = input("Seleccione una opcion:\n👉   ")
                        if op_info == "1":
                            print ("leer_descripcion")
                        elif op_info == "2":
                            print ("leer_info_contacto")
                        elif op_info == "3":
                            print ("leer_contrato")
                        elif op_info == "4": break
                    elif op_1_1_1 == "5": break
                    else: print ("opcion no valida")
            elif op_1_1 == "5": break
            else: print ("opcion no valida")
        
    elif op == "2": print ("Discografia") 
    elif op == "3": 
        print("Adios...")
        break
    else: print ("opcion no valida")
    
    



