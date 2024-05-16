"""
Ejercicio 26: Emular el funcionamiento de join para concatenar una lista.

numeros = [2, 3, 5, 7, 11]

235711

print(''.join([str(n) for n in numeros]))

"""


class EmuladorJoin:
    def __init__(self, lista):
        self.lista = lista
        self.cadena = ""

    def concatenar(self):
        for i in self.lista:
            i = str(i)
            self.cadena += i
        return self.cadena
    
lista_1 = EmuladorJoin([1,2,3,4,5,6,7,8,9])

print(lista_1.concatenar())