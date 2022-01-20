def obtener_precio(catalogo, producto):
    '''
    Tests:

    >>> catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
    >>> obtener_precio(catalogo, "pantalon_corto")
    13.5 
    '''
    pass #Eliminar esta línea

def total_compra(catalogo, carrito):
    '''
    Tests:

    >>> catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
    >>> carrito = [["camiseta roja", 1],["pantalon corto", 2], ["chaleco", 3]] 
    >>> total_compra(catalogo, carrito)
    81.5
    '''
    pass # Eliminar esta línea
    
def  mostrar_compra(catalogo, carrito):
    # completar funcion
    pass #Eliminar esta línea
    
# Programa principal
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


