from random import randint
def tirada():
    MIN_DICE = 1
    MAX_DICE = 6
    return [randint(MIN_DICE,MAX_DICE), randint(MIN_DICE,MAX_DICE)]
    

def puntuacion(dados, monedas):
    SUM_REINTEGRO = 8
    if dados[0] == dados[1]:
        return monedas * 2
    elif SUM_REINTEGRO <= (dados[0] + dados[1]):
        return 0
    else:
        return -monedas

def partida(m):
    # valido la apuesta
    num_monedas = 1
    while m != 0 and num_monedas != 0:
        num_monedas = int(input("Cuantas monedas quieres apostar: "))
        while num_monedas > m:
            print(f"Te quedan {m} monedas")
            num_monedas = int(input("Cuantas monedas quieres apostar: "))
        
        v_tirada = tirada()
        resultado = puntuacion(v_tirada, num_monedas)
        mensaje = f"Resultado {v_tirada[0]}, {v_tirada[1]}. "
        if resultado == 0:
            mensaje += "Ni ganas ni pierdes."
        elif resultado == -num_monedas:
            mensaje += "Pierdes."
        else:
            mensaje += "Ganaste."
        m += resultado
        mensaje += f"\nTe quedan {m} monedas."
        print(mensaje)
        if m > 0:
            num_monedas = int(input("Cuantas monedas quieres apostar: "))
    print(f"Terminas con {m} monedas")
    


    
# Programa principal

monedas = int(input("Con cuantas monedas quieres empezar: "))
partida(monedas)