# Ejercicio 66: Calcular el índice de masa corporal (IMC).

class IndiceMasaCorporal:
    def __init__(self, peso, estatura):
        self.peso = peso
        self.estatura = estatura
        
    def calcular(self):
        indice = self.peso / self.estatura ** 2
        return indice
    
    
persona1 = IndiceMasaCorporal(79.8, 1.78)
print(persona1.calcular())
    