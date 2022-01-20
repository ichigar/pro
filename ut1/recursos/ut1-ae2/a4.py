def obtener_precio(catalogo, producto):
    # completar función
    pass #Eliminar esta línea

def total_compra(catalogo, carrito):
    # completar función
    pass # Eliminar esta línea
    
def  mostrar_compra(catalogo, carrito):
    # completar funcion
    pass #Eliminar esta línea
    
# Programa principal

catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
carrito = [["camiseta roja", 1],["pantalon corto", 2], ["chaleco", 3]]

p_chaleco = obtener_precio(catalogo, "chaleco")
print(f"El precio del chaleco es de {p_chaleco}€.\n")

total = total_compra(catalogo, carrito)
print(f"El total de la compra es de: {total}€.\n")
            
print("El extracto de la compra en formato HTML es:\n")

mostrar_compra(catalogo, carrito)

