def count_phrases(text):
    """
    Función a la que se le pasa un texto y devuelve el número de frases que contiene
    El caracter delimitador de frases es el punto '.'
    Tests: 
    
    >>> texto = "Una frase. Dos frases. Tres frases."
    >>> count_phrases(texto)
    3
    """
    phrases = text.split('. ')
    
    return len(phrases)

def phrases_in_text(text):
    """
    Función a la que se le pasa un texto y devuelve una lista con las frases que contiene
    El caracter delimitador de frases es el punto '.'
    Tests:

    >>> phrases_in_text("Una frase. Dos frases. Tres, cuatro, cinco; seis. Y siete.")
    ['Una frase', 'Dos frases', 'Tres, cuatro, cinco; seis', 'Y siete.']
    """
    return text.split('. ')

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
    # Eliminamos signos de puntuación
    text = text.replace('.', '')
    text = text.replace(';', '')
    text = text.replace(',', '')
    
    # Pasar a minúscula texto
    text = text.lower()

    # Obtenemos lista de palabras
    lista = text.split()

    # Devolvemos lista ordenada

    return sorted(lista)

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
    # obtenemos lista de palabras en el texto
    words = ordered_words(text)

    # Calculamos palabras que terminan por la letra
    count = 0
    for word in words:
        if word[-1] == letter:
            count += 1
    # devolvemos contador
    return count

def delete_word(text, word):
    """
    función a la que le pasamos un texto y una palabra y devuelve el mismo texto
    sin que aparezca la palabra a eliminar.
    Tests:

    >>> delete_word("Uno dos tres cuatro Cinco", "dos")
    'Uno  tres cuatro Cinco'
    >>> delete_word("Uno, dos, tres; cuatro. Cinco", "dos")
    'Uno, , tres; cuatro. Cinco'
    """
    return text.replace(word, "")

