def valid_email(email):
    """
    validates email address
    :email:str
    :return:True|str
    """
    MIN_LENGTH = 6
    MIN_LENGTH_TLD = 2
    num_arroba = email.count('@')
    num_points = email.count('.')
    i_arroba = email.find('@')
    user_domain = email.split('@')
    last_item = user_domain[-1]
    domain_extension = email.split('.')
    tld = domain_extension[-1]
    

    # Comprobamos longitud mínima
    if len(email) < MIN_LENGTH:
        return 'longitud no válida'  

    #  Más de una @
    
    elif num_arroba != 1:
        return '@ no válida'
    
    # Empieza por @

    elif email.startswith('@'):
        return '@ no válida'

    # No contiene '.'
    
    elif num_points == 0:
        return 'dominio no válido'
    
    # No contiene '.' despues de la '@'
    elif last_item.find('.') == -1:
        return 'dominio no válido'
    
    # No tiene 2 o más caracteres después del último '.'
    elif len(tld) < MIN_LENGTH_TLD:
        return 'dominio no válido'

    # Pasa todas las pruebas (es válido)

    else:
        return True 