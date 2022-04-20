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
        for receta_json in file:                    # la líneas del fichero contienen texto en formato json
            receta = json.loads(receta_json)        # pasamos la línea a diccionario
            if receta["nombre"] == nombre_receta:
                print_receta(receta)
                return
        print("Receta no encontrada")

mostrar_receta("tortilla francesa")