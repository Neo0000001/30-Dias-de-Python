from random import choice, randrange

palabras = "coche,camion,tractor,armario,almacen".split(',')

# palabras = palabras.split(',')

print(palabras)
palabra = choice(palabras)
oculta = list(palabra)
palabra_mostrada = ""
print(oculta)
for i in range(int(len(palabra)*.6)):
    oculta[randrange(len(palabra))] = '_'

print(oculta)
