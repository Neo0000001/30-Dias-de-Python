# Ejercicio 59: Calcular la estatura (dada en pies y pulgadas) en centímetros.

# 1 ft = 30.48 cm
# 1 " = 2.54 cm

def calcular_estatura(pies, pulgadas):
    pies_a_centimetros = pies * 30.48
    pulgadas_a_centimetros = pulgadas * 2.54
    return pies_a_centimetros, pulgadas_a_centimetros

pies = 25
pulgadas = 25
estatura = calcular_estatura(pies, pulgadas)
print(f'{pies} pies equivale {estatura[0]} centimetros, {pulgadas} pulgadas equivale a {estatura[1]} centimetros.')    