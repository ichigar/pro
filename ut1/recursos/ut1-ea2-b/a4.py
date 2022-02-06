def num_vueltas(tiempos):
    return len(tiempos)

def total_vuelta(tiempos_vuelta):
    t_total = 0
    return round(sum(tiempos_vuelta), 2)

def vuelta_rapida(tiempos):
    t_min = total_vuelta(tiempos[0])
    i_min = 0
    for i in range(1, num_vueltas(tiempos)):
        if total_vuelta(tiempos[i]) < t_min:
            t_min = total_vuelta(tiempos[i])
            i_min = i
    return i_min

def vuelta_rapida_sectores(tiempos, i_sector):
    # completar función
    pass # Eliminar esta línea
    
def media_sectores(tiempos):
    # completar funcion
    pass #Eliminar esta línea


tiempos_alonso = [[12.45,21.56,8.34,31.54], [11.85,22.31,8.56,30.14], [13.05,21.43,8.34,31.54]]

# Mostramos el número de vueltas de alonso al circuito
n_v = num_vueltas(tiempos_alonso)
print(f"El número de vueltas fue de: {n_v}") # 3 

 # Mostramos el total de tiempo empleado en la vuelta 1
tiempos_alonso_vuelta1 = tiempos_alonso[0]
t_vuelta1 = total_vuelta(tiempos_alonso_vuelta1)
print(f"Tiempo empleado en vuelta 1: {t_vuelta1}") # 73.89

# # Mostramos la vuelta más rápida
i_vrapida = vuelta_rapida(tiempos_alonso)
print(f"La vuelta más rápida fue la número: {i_vrapida + 1}")  # 2

# # Mostramos el tiempo más rápido en el sector 3
# i_sector3 = 2
# t_min_sector3 = vuelta_rapida_sectores(tiempos_alonso, i_sector3) 
# print(f"El tiempo menor empleado en el sector 3 fue de: {t_min_sector3}")  # 8.34

# # Mostramos el tiempo medio en cada sector
# tiempos_medios = media_sectores(tiempos_alonso)
# print(f"El tiempo medio empleado en cada sector fue de: {tiempos_medios}")  # [12.45, 21.77, 8.41, 31.07]