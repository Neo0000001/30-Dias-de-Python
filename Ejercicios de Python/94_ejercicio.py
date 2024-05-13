# Ejercicio 94: Convertir una cadena de bytes en una lista de enteros.

cadena_bytes = b'Python'

lista_enteros = list(cadena_bytes)

print(lista_enteros)

# Python

"""
Este código muestra cómo convertir una cadena de bytes en una lista de enteros en Python.

En la primera línea, se define una variable llamada cadena_bytes que contiene la cadena de bytes b'Python'. La b al comienzo indica que es una 
cadena de bytes en lugar de una cadena de caracteres regular.

Luego, se utiliza la función list() para convertir la cadena de bytes en una lista de enteros. Cada elemento de la lista representa el valor 
entero correspondiente a cada byte en la cadena de bytes. Los enteros se basan en el valor ASCII de los caracteres.

Finalmente, se imprime la lista de enteros utilizando la función print(), lo cual produce el siguiente resultado:

[80, 121, 116, 104, 111, 110]

En este caso, la cadena de bytes 'Python' se convierte en una lista de enteros donde cada entero representa el valor ASCII del carácter 
correspondiente. Por ejemplo, el valor ASCII de 'P' es 80, el valor ASCII de 'y' es 121, y así sucesivamente.
"""
