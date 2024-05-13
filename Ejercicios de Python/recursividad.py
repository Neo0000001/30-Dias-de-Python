def funcion(x):
    print('Esto es una funcion recursiva... ')
    x = x + 1
    print(x)
    if x == 3:
        print('Recursibidad terminada...')
        exit()

    funcion(x)


x = 0
funcion(x)
