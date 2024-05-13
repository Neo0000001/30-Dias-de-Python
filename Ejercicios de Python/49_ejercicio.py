# Ejercicio 49: Mostrar los archivos de un directorio específico.

from os.path import isfile, join
from os import listdir

class MostrarArchivos:
    def __init__(self, ruta):
        self.ruta = ruta
        
    def listar_directorios(self):
        archivos = [archivo for archivo in listdir(self.ruta) if isfile(join(self.ruta, archivo))]
        return archivos

ruta = r"/home/enrique/Hello world/Python"

listado_1 = MostrarArchivos(ruta)
print(listado_1.listar_directorios())


