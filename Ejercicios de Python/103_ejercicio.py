# Ejercicio 103: Obtener el nombre de archivo de una ruta absoluta.

import os

ruta = r'/home/enrique/Documentos/express-project/100_ejercicio.py'

nombre_archivo = os.path.basename(ruta)

print(nombre_archivo)
