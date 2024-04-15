# Ejercicio 95: Comprobar si una cadena de caracteres representa un número.


def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except (TypeError, ValueError):
        return False


cadena = '2.7182'

print(es_numerico(cadena))

cadena = '3.1415ab'

print(es_numerico(cadena))

cadena = (5.3, 7.9)

print(es_numerico(cadena))

"""
La función es_numerico()toma una cadena como entrada y devuelve Truesi la cadena representa un número y Falsesi no. La función funciona al 
intentar convertir la cadena en un flotante. Si la conversión es exitosa, la función devuelve True. De lo contrario, la función devuelve False.

En el primer ejemplo, la cadena '2.7182'representa un número, por lo que la función devuelve True. En el segundo ejemplo, la cadena '3.1415ab'
no representa un número, por lo que la función devuelve False. En el tercer ejemplo, la cadena (5.3, 7.9)es una tupla, no una cadena, por lo 
que la función devuelve False.
"""
