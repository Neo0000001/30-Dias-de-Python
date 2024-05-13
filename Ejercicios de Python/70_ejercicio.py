# Ejercicio 70: Ordenar un conjunto de archivos por fecha de creación.

import glob
import os

ruta = r'/home/enrique/Hello world/Python/30 dias de Python/100_Ejercicios python/'

archivos = glob.glob(ruta + os.path.sep + '*.py')

archivos.sort(key = os.path.getctime)

print('\n'.join(archivos))