# Ejercicio 107: Obtener las propiedades básicas de un archivo.

import os
import time

archivo = 'PyWhatKit_DB.txt'

print('Archivo:', archivo)
print(f'Fecha modificación: {(time.ctime(os.path.getmtime(archivo)))}')
print('Fecha acceso: {}'.format(time.ctime(os.path.getatime(archivo))))
print('Fecha cambio: {}'.format(time.ctime(os.path.getctime(archivo))))
print('Tamaño: %d bytes' % os.path.getsize(archivo))