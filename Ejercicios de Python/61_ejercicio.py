# Ejercicio 61: Convertir todas las unidades de tiempo en segundos.

dias = int(input('Introduce el numero de dias: '))
horas = int(input('Introduce el numero de horas: '))
minutos = int(input('Introduce el numero de minutos: '))
segundos = int(input('Introduce el numero de segundos: '))

segundos += dias * 24 * 60 * 60
segundos += horas * 60 * 60
segundos += minutos * 60
#segundos += segundos

print(f'El numero total de segundos es {segundos}')