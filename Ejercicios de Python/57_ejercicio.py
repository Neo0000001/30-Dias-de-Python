# Ejercicio 57: Medir el tiempo de ejecución de un método.

import time

def sumar_rango(n):
    
    t1 = time.time()
    
    suma = 0
    for i in range(n):
        suma += 1
        
    t2 = time.time()
    
    tiempo_ejecucion = t2 -t1
    return tiempo_ejecucion

n = 100000

print(sumar_rango(n))

n = 1000000

print(sumar_rango(n))
 