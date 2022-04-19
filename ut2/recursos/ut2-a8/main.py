from os import system
from urbanizacion import *

u_sol = UrbanizacionSol()

opcion = 1

while opcion != 0:
    system("clear")
    print("1. Añadir propiedad")
    print("2. Checkin")
    print("3. Checkout")
    print("4. Mostrar viviendas libres")
    print("5. Mostrar vivienda")
    print("6. Mostrar saldo")
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        u_sol.nueva_vivienda()
    
    elif opcion == 2:
        nombre_vivienda = input("nombre de la vivienda: ")
        num_dias = int(input("Número de días: "))
        u_sol.checkin(nombre_vivienda, num_dias)
    
    elif opcion == 3:
        nombre_vivienda = input("nombre de la vivienda: ")
        u_sol.checkout(nombre_vivienda)
    
    elif opcion == 4:
        u_sol.viviendas_libres()
    
    elif opcion == 5:
        nombre_vivienda = input("nombre de la vivienda: ")
        u_sol.mostrar_vivienda(nombre_vivienda)
    
    elif opcion == 6:
        u_sol.mostrar_saldo()
    
    else:
        print("Opción incorrecta")
    
    input("Pulsa Enter para continuar ")