# Ejercicio 87: Obtener el tamaño de un archivo.

import os
ruta = r'D:\Dropbox\Downloads\Software\Hirens.BootCD.15.2.zip'


archivo_bytes = os.path.getsize(ruta)

print(archivo_bytes)
