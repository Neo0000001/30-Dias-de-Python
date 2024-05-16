# Ejercicio 84: Contar la cantidad de ocurrencias de un carácter en una cadena de caracteres.

cadena = 'Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.'

diccionario = {}

for i in cadena:
    cantidad = cadena.count(i)
    diccionario[f'Caracter {i}'] = cantidad
    # print(f'El caracter {i}, aparece {cantidad} veces')

print(diccionario)
