def valid_passwd(passwd):
    """
    function tests
    >>> valid_passwd("lej50*paRapa")
    True
    >>> valid_passwd("lej50*pa")
    ['longitud < 10']

    >>> valid_passwd('12345')
    ['longitud < 10', 'no contiene mayúsculas', 'no contiene caracteres especiales']
    """
    # Inicialización de variables
    valid = True
    messagges = []
    
    # Comprobación longitud
    if len(passwd) < 10:
        messagges.append("longitud < 10")
        valid = False
    # Comprobación mayúsculas
    if passwd == passwd.lower():
        messagges.append("no contiene mayúsculas")
        valid = False
    # Comprobación especiales
    special_chars = "*#+-.,()[]{}"
    has_special_chars = False
    for character in passwd:
        if character in special_chars:
            has_special_chars = True
    if not has_special_chars:
        messagges.append("no contiene caracteres especiales")
        valid = False
    # Generamos salida de la función
    if valid:
        return True
    else:
        return messagges

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

