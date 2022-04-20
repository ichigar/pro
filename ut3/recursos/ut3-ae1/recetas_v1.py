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

def existe_receta(nombre_receta):
    with open(FILE_RECETAS,"r") as file:
        for receta_json in file:
            receta = json.loads(receta_json)
            if receta["nombre"] == nombre_receta:
                return True
        return False

def nueva_receta(nombre_receta, tiempo, lista_ingredientes): 
    if not existe_receta(nombre_receta):
        receta = {
            "nombre": nombre_receta,
            "tiempo": tiempo,
            "ingredientes": lista_ingredientes
        }
        with open(FILE_RECETAS, "a") as file:
            file.write("\n" + json.dumps(receta))
        return True
    return False

# if nueva_receta("arbejas", 15, ["arbejas", "zanahoria", "aceite", "sal"]):
#     print("Receta añadida")
# else:
#     print("Receta ya existe")

def escribir_recetas(recetas):
    with open(FILE_RECETAS, "w") as file:
        for i in range(len(recetas) - 1):
            file.write(json.dumps(recetas[i]) + "\n")
        file.write(json.dumps(recetas[-1])) # No incluimos el \n al final

def añadir_ingrediente(nombre_receta, ingrediente):
    if existe_receta(nombre_receta):
        # Leemos las recetas y localizamos la que queremos modificar
        with open(FILE_RECETAS, "r") as file:
            recetas_json = file.readlines()
            recetas = []
            for receta_json in recetas_json:
                receta = json.loads(receta_json)
                if receta["nombre"] == nombre_receta:
                    if ingrediente not in receta["ingredientes"]:
                        receta["ingredientes"].append(ingrediente)
                    else:
                        return False    # El ingrediente ya existe
                recetas.append(receta)
        
        escribir_recetas(recetas)
        return True
    return False    # La receta no existe

# if añadir_ingrediente("tortilla francesa", "jamon"):
#     print("Receta modificada")
# else:
#     print("Receta no existe o ya contienen el ingrediente")

def eliminar_receta(nombre_receta):
    if existe_receta(nombre_receta):
        # Leemos las recetas y localizamos la que queremos eliminar
        with open(FILE_RECETAS, "r") as file:
            recetas_json = file.readlines()
            recetas = []
            for receta_json in recetas_json:
                receta = json.loads(receta_json)
                if receta["nombre"] != nombre_receta:
                    recetas.append(receta)
        
        escribir_recetas(recetas)
        return True
    return False    # La receta no existe

# if eliminar_receta("tortilla francesa"):
#     print("Receta eliminada")
# else:
#     print("Receta no existe")