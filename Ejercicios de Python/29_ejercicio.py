# Ejercicio 29: Calcular el área de un triángulo.

class AreaTriangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) / 2
    
triangulo_1 = AreaTriangulo(20, 10)
print(triangulo_1.area())