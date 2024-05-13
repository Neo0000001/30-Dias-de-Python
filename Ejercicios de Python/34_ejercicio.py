# Ejercicio 34: Validar Dos Números. Si son iguales o la suma o el valor absoluto son 5.

class ValidarDosNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def validar(self):
        if self.a == self.b or self.a + self.b == 5 or abs(self.a - self.b) == 5:
            return True
        else:
            return False
        
bloque_1 = ValidarDosNumeros(5, 5)
bloque_2 = ValidarDosNumeros(2, 3)
bloque_3 = ValidarDosNumeros(16, 11)
bloque_4 = ValidarDosNumeros(3, 4)

print(bloque_1.validar())
print(bloque_2.validar())
print(bloque_3.validar())
print(bloque_4.validar())