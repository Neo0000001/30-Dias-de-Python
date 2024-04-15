# Ejercicio 40: Calcular la distancia entre dos puntos cartesianos.

# P1(x1, y1), P2(x2, y2)

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return math.sqrt(dx**2 + dy**2)

# creamos dos objetos de la clase Punto
p1 = Punto(2, 3)
p2 = Punto(5, 7)

# calculamos la distancia entre los dos puntos
distancia = p1.distancia(p2)

print("La distancia entre los puntos ({}, {}) y ({}, {}) es {:.2f}".format(p1.x, p1.y, p2.x, p2.y, distancia))
