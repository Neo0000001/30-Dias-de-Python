# Ejercicio 111: Seleccionar archivos de un tipo específico.

import glob
import os

ruta = r'/home/enrique/Documentos/express-project/30 dias de Python/Ejercicios python'

comodin = '*.py'

lista_archivos = glob.glob(ruta + os.sep + comodin)

ordenado_en_columna = '\n'.join(lista_archivos)

print(ordenado_en_columna)