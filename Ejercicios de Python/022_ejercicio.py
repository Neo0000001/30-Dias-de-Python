"""
 Ejercicio 22: Crear una subcadena de n caracteres replicada n cantidad de veces.

'Python', n = 2 => 'Py'; 'PyPy'
"""


class GeneradorCadenas:
    def __init__(self,cadena, n) -> None:
        self.cadena = cadena
        self.n = n
        
    def generador(self):
        subcadena = self.cadena[:self.n]
        print(subcadena * self.n)
            
cadena_1 = GeneradorCadenas('Euromaster', 5)
cadena_1.generador()
            
        