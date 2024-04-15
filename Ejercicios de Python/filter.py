def es_mayor_a_cinco(numero):
    return numero > 5


numeros = [1, 6, 3, 8, 2, 9]
numeros_filtrados = list(filter(es_mayor_a_cinco, numeros))

print(numeros_filtrados)
