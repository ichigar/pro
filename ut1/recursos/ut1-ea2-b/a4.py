def num_vueltas(tiempos):
    return len(tiempos)

def total_vuelta(tiempos_vuelta):
    t_total = 0
    return round(sum(tiempos_vuelta), 2)

def vuelta_rapida(tiempos):
    # Tomamos como referencia la suma de tiempos de sectores de la primera vuelta
    t_min = total_vuelta(tiempos[0])
    i_min = 0   # Guardamos el índice de la vuelta con tiempo mínimo
    for i in range(1, num_vueltas(tiempos)):
        # Miramos para cada vuelta si el tiempo es menor que el de las anteriores
        if total_vuelta(tiempos[i]) < t_min:
            # Guardamos el nuevo tiempo mínimo y el índice de la vuelta en que se produce
            t_min = total_vuelta(tiempos[i])
            i_min = i
    return i_min

def vuelta_rapida_sectores(tiempos, j_sector):
    # OPCION ALTERNATIVA
    # aux = []
    # for vuelta in tiempos:
    #     t_sector = vuelta[j_sector]
    #     print(f"------------{t_sector}")
    #     aux.append(t_sector)
    # return min(aux)

    # tomamos como primera referencia el tiempo en la primera vuelta en el sector buscado
    t_min = tiempos[0][j_sector]        
    for vuelta in tiempos:
        t_sector = vuelta[j_sector]
        # Miramos para cada vuelta si el tiempo en el sector es menor que el que teníamos
        if t_sector < t_min:
            t_min = t_sector
    return t_min

def media_sectores(tiempos):
    
    result = tiempos[0]  # Almacenará lista con los valores medios de cada sector. Empezamos con los valores de la primera vuelta
    num_sectores = len(result)

    for i in range(1, num_vueltas(tiempos)):    # recorremos todas las vueltas
        for j in range(num_sectores):           # recorremos los sectores de cada vuelta
            result[j] += tiempos[i][j]          # sumamos los tiempos de cada sector a los que ya teníamos
    for j in range(num_sectores):
        # Calculamos media de cada sector. Dividiendo suma de tiempos por el número de vueltas
        # Redondeamos resultado a 2 decimales
        result[j] = round(result[j] / num_vueltas(tiempos), 2)   
    return result


tiempos_alonso = [  [12.45,21.56,8.34,31.54], 
                    [11.85,22.31,8.56,30.14], 
                    [13.05,21.43,8.34,31.54]]

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

#  Mostramos el tiempo más rápido en el sector 3
j_sector2 = 1
t_min_sector2 = vuelta_rapida_sectores(tiempos_alonso, j_sector2) 
print(f"El tiempo menor empleado en el sector 3 fue de: {t_min_sector2}")  # 21.43

# Mostramos el tiempo medio en cada sector
tiempos_medios = media_sectores(tiempos_alonso)
print(f"El tiempo medio empleado en cada sector fue de: {tiempos_medios}")  # [12.45, 21.77, 8.41, 31.07]
