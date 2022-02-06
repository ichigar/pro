from a1 import *
from a2 import *
from a3 import *
from a4 import *
def main():
    # a1.py - comprobaciones
    print(valid_passwd("lej50*paRapa"))
    print(valid_passwd("lej50*pa"))
    print(valid_passwd('12345'))

    # a2.py - comprobaciones
    count_phrases("Una frase. Dos frases. Tres frases. ")
    phrases_in_text("Una frase. Dos frases. Tres, cuatro, cinco; seis. Y siete.")
    ordered_words("Uno dos tres cuatro Cinco")
    ordered_words("Uno, dos, tres; cuatro. Cinco")
    n_words_end_in("o", "Uno dos tres cuatro Cinco")
    n_words_end_in("o", "Uno, dos, tres; cuatro. Cinco")

    # a3.py - comprobaciones
    monedas = 4
    n_tiradas = 5
    p_final = partida(monedas, n_tiradas)
    print(f"Has finalizado con {p_final} monedas")
    delete_word("dos", "Uno dos tres cuatro Cinco")
    delete_word("dos", "Uno, dos, tres; cuatro. Cinco")

    # a4.py - comprobaciones
    catalogo = [["camiseta roja", 10.50], ["camiseta azul", 10.99], ["camiseta blanca", 9.90],["pantalon vaquero", 21.50], ["pantalon corto", 13.50], ["chaleco", 17.20]]
    carrito = [["camiseta roja", 1],["pantalon corto", 2], ["chaleco", 3]]

    p_chaleco = obtener_precio(catalogo, "chaleco")
    print(f"El precio del chaleco es de {p_chaleco}€.\n")

    total = total_compra(catalogo, carrito)
    print(f"El total de la compra es de: {total}€.\n")
                
    print("El extracto de la compra en formato HTML es:\n")

    mostrar_compra(catalogo, carrito)

if __name__ == '__main__':
    main()