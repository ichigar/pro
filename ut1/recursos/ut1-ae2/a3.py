from random import randint

def puntuacion(a, b, c):
    '''
    Tests:

    >>> puntuacion(2, 2, 2)
    5
    >>> puntuacion(1, 2, 2)
    2
    >>> puntuacion(2, 1, 2)
    2
    >>> puntuacion(2, 2, 1)
    2
    >>> puntuacion(1, 2, 3)
    0
    '''
    # Completar el código de esta función
    if a == b and b == c:
        return 5
    if a != b and b != c and a != c:
        return 0
    return 2
    

def partida(m, n):
    i = 0
    while i < n and m > 0:
        i += 1   # contador de tiradas
        m -= 1   # Al hacer una tirada perdemos una moneda
        n1, n2, n3 = randint(1, 5), randint(1, 5), randint(1, 5)
        points = puntuacion(n1, n2, n3) # calculamos puntuación tirada
        m += points # actualizamos monedas
        # mostramos la tirada
        print(f"Tirada {i}: {n1} - {n2} - {n3} -> monedas: {m}")

    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
