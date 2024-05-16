# Ejercicio 68: Sumar los dígitos de un número entero positivo.

numero = input('Introduce un numero entero positivo: ')
lista_digitos = list(numero)
print(lista_digitos)
lista_digitos = [int(i) for i in lista_digitos]
    
suma = sum(lista_digitos)
print(suma)