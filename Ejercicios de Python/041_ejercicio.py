# Ejercicio 41: Comprobar si un archivo existe.

import os

class VerificarArchivo:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comprobar(self):
        return os.path.isfile(self.nombre)
    
archivo_1 = VerificarArchivo('40_ejercicio.py')

print(archivo_1.comprobar())