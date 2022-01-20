def obtener_precio(catalogo, nombre_producto):
    '''
    Tests:

    >>> catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
    >>> obtener_precio(catalogo, "pantalon_corto")
    13.5 
    '''
    for producto in catalogo:
        if producto[0] == nombre_producto:
            return producto[1]

def total_compra(catalogo, carrito):
    '''
    Tests:

    >>> catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
    >>> carrito = [["camiseta roja", 1],["pantalon corto", 2], ["chaleco", 3]] 
    >>> total_compra(catalogo, carrito)
    81.5
    '''
    total = 0
    for item in carrito:
        nombre_producto = item[0]
        precio = obtener_precio(catalogo, nombre_producto)
        cantidad = item[1]
        total += precio * cantidad
    return total
def  mostrar_compra(catalogo, carrito):
    # completar funcion
    
    html = '''
    <table>
        <tr>
            <th>Producto</th><th>cantidad</th><th>P U</th><th>P Total</th>
        </tr>
    '''
    for item in carrito:
        precio = obtener_precio(catalogo, item[0])
        total = item[1] * precio
        html += "<tr>\n"
        html += "<td>" + item[0] + "</td><td>" + str(item[1]) + "</td><td>" + str(precio) + "</td><td>" + str(total) + "</td>\n"
        html += "</tr>\n"
    html += "</table>"
    return html

    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)