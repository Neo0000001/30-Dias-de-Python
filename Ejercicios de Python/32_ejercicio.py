# Ejercicio 32: Calcular la suma de tres números si todos son diferentes, en caso contrario la suma será 0.

class SumaTresNumeros:
    def __init__(self, a, b, c,) -> None:
        self.a = a
        self.b = b
        self.c = c
        
    def suma(self):
        if self.a == self.b == self.c:
            return self.a + self.b + self.c
        else:
            return 0
        
suma_1 = SumaTresNumeros(3, 3, 3)
print(suma_1.suma())
suma_2 = SumaTresNumeros(1, 2, 3)
print(suma_2.suma())