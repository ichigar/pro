def count_phrases(text):
    """
    Función a la que se le pasa un texto y devuelve el número de frases que contiene
    El caracter delimitador de frases es el punto '.'
    Tests: 
    >>> count_phrases("Una frase. Dos frases. Tres frases. ")
    3
    """
    return len(text.split(". "))
    
def phrases_in_text(text):
    """
    Función a la que se le pasa un texto y devuelve una lista con las frases que contiene
    El caracter delimitador de frases es el punto '.'
    Tests:

    >>> phrases_in_text("Una frase. Dos frases. Tres, cuatro, cinco; seis. Y siete.")
    ['Una frase', 'Dos frases', 'Tres, cuatro, cinco; seis', 'siete']
    """
    # Completar código
    pass # Eliminar esta línea
    
 
def ordered_words(text):
    """
    Función a la que le pasamos un texto y devuelve una lista con las palabras que contiene
    La lista debe estar ordenada alfabéticamente
    Todas las palabras deben estar en minúscula
    
     >>> ordered_words("Uno dos tres cuatro Cinco")
    ['cinco', 'cuatro', 'dos', 'tres', 'uno']
    >>> ordered_words("Uno, dos, tres; cuatro. Cinco")
    ['cinco', 'cuatro', 'dos', 'tres', 'uno']
    """
    # Elimina mos signos de puntuación

    # Pasamos a minúscula

    # Obtenemos lista de palabras

    # Ordenamos la lista y la devolvemos
    pass # Eliminar esta línea
    
def n_words_end_in(letter, text):
    """
    Función a la que se le pasa una letra y un texto y devuelve el número
    de palabras del texto que terminan por dicho carácter
    Tests:

    >>> n_words_end_in("o", "Uno dos tres cuatro Cinco")
    3
    >>> n_words_end_in("o", "Uno, dos, tres; cuatro. Cinco")
    3
    """
    # Completar código
    pass # Eliminar esta línea

def delete_word(text, word):
    """
    función a la que le pasamos un texto y una palabra y devuelve el mismo texto
    sin que aparezca la palabra a eliminar.
    Tests:

    >>> delete_word("dos", "Uno dos tres cuatro Cinco")
    'Uno  tres cuatro Cinco'
    >>> delete_word("dos", "Uno, dos, tres; cuatro. Cinco")
    'Uno, , tres; cuatro. Cinco'
    """
    # Completar código
    pass # Eliminar esta línea
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
