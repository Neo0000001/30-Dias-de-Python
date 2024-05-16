# Ejercicio 48: Convertir una cadena de caracteres a entero y real.

# int(), float()

cadena = '3.1415'
"""
Convertivos la cadena en una lista con el metodo split(), utilzamos el caracter '.' como separador, y que nos muestre el primer elemento 
de la primera lista, y lo transformamos a entero con int()
"""
entero = int(cadena.split('.')[0]) 
print(entero)

cadena = float(cadena)
print(cadena)