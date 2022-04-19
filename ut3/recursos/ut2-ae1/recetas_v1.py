import json

FILE_RECETAS = "recetas_v1.txt"

def mostrar_receta(nombre_receta):
    with open(FILE_RECETAS, "r") as file:
        for receta_json in file:
            receta = json.loads(receta_json)
            if receta["nombre"] == nombre_receta:
                print(f"Nombre: {receta['nombre']}")
                print(f"Tiempo: {receta['tiempo']} minutos")
                print("Ingredientes:")
                for ingrediente in receta["ingredientes"]:
                    print(f"* {ingrediente}")

mostrar_receta("tortilla francesa")