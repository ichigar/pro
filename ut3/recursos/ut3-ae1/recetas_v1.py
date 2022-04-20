import json

FILE_RECETAS = "recetas_v1.txt"

def print_receta(receta):
    print(f"Nombre: {receta['nombre']}")
    print(f"Tiempo: {receta['tiempo']} minutos")
    print("Ingredientes:")
    for ingrediente in receta["ingredientes"]:
        print(f"* {ingrediente}")

def mostrar_receta(nombre_receta):
    with open(FILE_RECETAS, "r") as file:
        recetas = file.readlines()                  # Leemos líneas a lista
        for receta_json in recetas:                 # la líneas del fichero contienen texto en formato json
            receta = json.loads(receta_json)        # pasamos la línea a diccionario
            if receta["nombre"] == nombre_receta:
                print_receta(receta)
                return
        print("Receta no encontrada")

# mostrar_receta("tortilla francesa")

def lista_en_lista(lista, lista_buscar):
    """Comprueba si todos los elementos de lista están en lista_buscar """
    
    for item in lista:
        if item not in lista_buscar:
            return False
    return True

def mostrar_receta_ingredientes(lista_ingredientes):
    with open(FILE_RECETAS,"r") as file:
        recetas = file.readlines()
        for receta_json in recetas:                 
            receta = json.loads(receta_json)
            ingredientes_receta = receta["ingredientes"]   # Extraemos los ingredientes de la receta que estamos recorriendo
            
            # Comprobamos si todos los ingredientes que buscamos están en la receta
            if lista_en_lista(lista_ingredientes, ingredientes_receta):
                mostrar_receta(receta["nombre"])
                
# mostrar_receta_ingredientes(["aceite", "sal", "huevos"])

def nueva_receta(nombre_receta, tiempo, lista_ingredientes): 
    with open(FILE_RECETAS,"a") as file:    # Abrimos el fichero en modo append
        receta = {
            "nombre":nombre_receta, 
            "tiempo":tiempo, 
            "ingredientes":lista_ingredientes
        }
        
        file.write("\n" + json.dumps(receta))   # Escribimos el diccionario en formato json

nueva_receta("arbejas", 15, ["arbejas", "zanahoria", "aceite", "sal"])