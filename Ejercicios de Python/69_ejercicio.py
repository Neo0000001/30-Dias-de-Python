# Ejercicio 69: Ordenar tres números de menor a mayor sin usar condicionales ni ciclos.

a = int(input('Introduce el primer numero: '))
b = int(input('Introduce el segundo numero: '))
c = int(input('Introcude el tercer numer: '))

lista = (a, b, c)
lista = list(lista)
print(f'Numeros introducidos: {lista}')
lista.sort()
print(f'Lista ordenada: {lista}')
mayor = max(lista)
menor = min(lista)
print(f'Los numeros ordenados son {menor}, {lista[1]}, {mayor}')