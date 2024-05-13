"""
Ejercicio 27: Generar un conjunto de números aleatorios y determinar cuáles son impares.

k mod 2 == 1
"""

class NumerosImpares():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.numeros_impares = []
        
    def impares(self):
        from random import randint
        numeros_aleatorios = [randint(self.a, self.b) for i in range(100)]
        for i in numeros_aleatorios:
            if i % 2 != 0:
                self.numeros_impares.append(i)
        return self.numeros_impares
    
numeros_1 = NumerosImpares(3, 650)
print(numeros_1.impares())
            