# Ejercicio 92: Filtrar números por medio de la función filter.


numeros = [i for i in range(10)]
print(numeros)


def filtro_impares(x):
    return x % 2 == 1


impares = filter(filtro_impares, numeros)

print(list(impares))

# Otro ejercicio


def es_mayor_a_cinco(numero):
    return numero > 5


numeros = [1, 6, 3, 8, 2, 9]
numeros_filtrados = list(filter(es_mayor_a_cinco, numeros))

print(numeros_filtrados)

"""
En este ejemplo, definimos una función es_mayor_a_cinco() que devuelve True si el número es mayor que 5. Luego, utilizamos la función filter() 
para filtrar los números de la lista numeros y obtener solo aquellos que son mayores que 5. El resultado se convierte en una lista y se imprime.

La salida del ejemplo sería [6, 8, 9], ya que son los números mayores que 5 en la lista original.

Ten en cuenta que el código real del ejercicio que mencionas debería contener la función de filtro específica y la secuencia en la que se aplica 
la función. Sin ese código, no puedo proporcionarte una explicación más detallada.

La función filter() se utiliza para filtrar elementos de una secuencia (como una lista) según una condición específica. Toma dos argumentos: una 
función de filtro y una secuencia. La función de filtro debe ser una función que devuelve un valor booleano (True o False) y se aplica a cada 
elemento de la secuencia.

La función filter() devuelve un objeto de filtro, que puede convertirse en una lista o en otro tipo de secuencia según sea necesario.
"""
