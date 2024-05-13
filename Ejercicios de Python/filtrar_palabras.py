"""Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]
    

lista_palabras = ['coche', 'avion', 'tren', 'autobus', 'uva', 'cafe']
n = 3      
resultado = filtrar_palabras(lista_palabras, n)
print(resultado)