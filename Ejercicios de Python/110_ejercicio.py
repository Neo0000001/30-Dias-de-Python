# Ejercicio 110: Obtener los números divibles por 7 usando una función anónima.

numeros = [3, 14, 29, 42, 70, 2, 7, 8, 9, 13]

divisible_por_7 = lambda x: x % 7 == 0

num_div_por_7 = list(filter(divisible_por_7, numeros))

print(num_div_por_7)