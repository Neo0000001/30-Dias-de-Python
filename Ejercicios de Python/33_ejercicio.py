# Ejercicio 33: Sumar dos números. Si la suma está entre 10 y 30, retornar 30.

class SumaDosNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def suma(self):
        suma = self.a + self.b
        if suma >= 10 and suma <= 30:
            return 30
        else:
            return suma
        
suma_1 = SumaDosNumeros(10, 20)
print(suma_1.suma())
suma_2 = SumaDosNumeros(20, 60)
print(suma_2.suma())