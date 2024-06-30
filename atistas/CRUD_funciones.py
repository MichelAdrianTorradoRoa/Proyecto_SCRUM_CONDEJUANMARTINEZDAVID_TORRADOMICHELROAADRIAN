from funciones_secundarias import print_
import csv

def genero_canciones(canciones):    
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
            
def contador_id():
    class idARTISTA:
        def __init__(self, archivo):
            self.archivo = archivo
            self.id_id = self.cargar_id()
        def cargar_id(self):
            try:
                with open(self.archivo, 'r') as f:
                    reader = csv.reader(f)
                    return int(next(reader)[0])
            except FileNotFoundError:
                return 0
        def guardar_id(self):
            with open(self.archivo, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['{:02d}'.format(self.id_id)])
        def registrar_artistas(self):
            self.id_id += 1
            self.guardar_id()
        def obtener_id(self):
            return '{:02d}'.format(self.id_id)
    id = idARTISTA('id_artista.csv')
    id.registrar_artistas()
    id_artista = id.obtener_id()
    return id_artista

# print (contador_id())