# Ejercicio 89: Generar números aleatorios y verificar que todos sean impares.

from random import randint


def generar_impares(n=5):
    impares = []

    while True:
        numeros = [randint(1, 100) for _ in range(n)]

        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break

    return impares


impares = generar_impares()

print(impares)

print(generar_impares(20))

# Mi version


def generador_aleatorio_impar(n):

    numeros = []

    while len(numeros) <= n:
        aleatorio = randint(1, 100)
        if aleatorio % 2 == 1:
            numeros.append(aleatorio)

    print(numeros)


generador_aleatorio_impar(20)
