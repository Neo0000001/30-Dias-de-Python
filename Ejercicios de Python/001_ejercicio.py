"""
Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def es_primo(numero):
    """
    Comprueba si un número es primo.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_fibonacci(numero):
    """
    Comprueba si un número está en la secuencia de Fibonacci.
    """
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def es_par(numero):
    """
    Comprueba si un número es par.
    """
    return numero % 2 == 0

def comprobacion(numero):
    if es_primo(numero):
        primo_texto = "primo"
    else:
        primo_texto = "no es primo"

    if es_fibonacci(numero):
        fibonacci_texto = "fibonacci"
    else:
        fibonacci_texto = "no es fibonacci"

    if es_par(numero):
        par_texto = "par"
    else:
        par_texto = "impar"

    print(f"{numero} es {primo_texto}, {fibonacci_texto} y es {par_texto}")
    
comprobacion(numero = int(input("Introduce un número: ")))