# Ejercicio 93: Obtener el número de ID de un objeto.

numeros = [2, 3, 5]

print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))
print(id(numeros))


def mostrar_id(objeto):
    print(id(objeto))


mostrar_id(numeros)

objeto = object()

mostrar_id(objeto)

"""
En Python, casi todo es un objeto. Python es un lenguaje de programación orientado a objetos, lo que significa que los datos y el código se 
organizan en objetos que representan entidades del mundo real. Los objetos son instancias de clases, que son estructuras que definen las 
propiedades y el comportamiento de un objeto.

En Python, incluso los tipos de datos primitivos, como enteros, cadenas y listas, son objetos. Estos objetos primitivos tienen métodos y 
propiedades asociadas que se pueden utilizar para manipular y trabajar con ellos.

Por ejemplo, los objetos de tipo cadena (str) tienen métodos como upper(), lower(), split(), entre otros, que se pueden llamar para realizar 
operaciones en las cadenas. Los objetos de tipo lista (list) tienen métodos como append(), remove(), sort(), entre otros, para manipular la lista.

Además, en Python, se pueden crear y definir clases personalizadas para crear nuevos objetos con propiedades y métodos específicos. Estas clases 
se utilizan para crear instancias de objetos, y las instancias pueden acceder a los atributos y métodos definidos en la clase.

Sin embargo, hay algunas excepciones en las que los elementos no son objetos en Python. Por ejemplo, las palabras clave (keywords) del lenguaje, 
como if, else, for, no son objetos. Además, los operadores aritméticos y los operadores lógicos, como +, -, *, /, and, or, tampoco son objetos.

En resumen, en Python, la mayoría de los elementos, incluidos los tipos de datos y las estructuras, son objetos y se pueden manipular utilizando 
sus métodos y propiedades. Esto es una de las características que hacen que Python sea un lenguaje versátil y flexible.
"""
