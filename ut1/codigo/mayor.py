n_valores = int(input("¿Cuántos valores quieres leer? "))
if n_valores == 0:
    print("No se lee ningún valor. No hay valor mayor")
else:
    max = int(input("Introduce el valor 1: "))
    for i in range(n_valores - 1):
        valor = int(input(f"Introduce el valor {i + 2}: "))
        if valor > max:
            max = valor
    print(f"El valor mayor leido es {max}")