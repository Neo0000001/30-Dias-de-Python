# Ejercicio 112: Eliminar un elemento específico de una lista.

colores = ['Rojo', 'Verde', 'Azul', 'Naranja', 'Negro', 'Blanco']

elemento_a_eliminar = int(input('Ingrese el indice del elemento a eliminar: '))

print(f'El elemento a eliminar es: {colores[elemento_a_eliminar]}')

del colores[elemento_a_eliminar]

print(f'Ahora la lista queda así: {colores}, y contiene {len(colores)} elementos')