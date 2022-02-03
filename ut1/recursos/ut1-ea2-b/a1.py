def valid_email(email):
    """
    validates email address
    :email:str
    :return:True|str
    """
    # Completar código de la función
    pass # eliminar esta línea

# Ejemplos de ejecución y resultado
print(valid_email("a@a"))                    # 'longitud no válida'
print(valid_email("user@dom@dom.es"))        # '@ no válida'
print(valid_email("@user.com"))              # '@ no válida'
print(valid_email("user@ab.c"))              # 'dominio no válido'
print(valid_email("user@.com"))              # 'dominio no válido'
print(valid_email("user.2000@rediris.es"))   # True