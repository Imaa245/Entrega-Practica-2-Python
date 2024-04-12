def ordenar (nombres, goles, goles_evit, asist):
    
    jugadores = {}
    nombres = nombres.replace(',', '').split()
    for nom, gol, gol_evi, a in zip(nombres, goles, goles_evit, asist):
        jugadores[nom] = (gol, gol_evi, a)
    return jugadores

def max_goleador (jugadores):
    goleador, goles = max(jugadores.items(), key= lambda maximo: maximo[1][0])
    return goleador, goles[0]

def mas_influyente (jugadores):
    maximo = -1
    nombre_max = None
    for nombre, stats in jugadores.items():
        promedio = (stats[0]*1.50) + (stats[1]*1.25) + (stats[2])
        if (promedio > maximo):
           nombre_max = nombre
           maximo = promedio
    return nombre_max, maximo

def promedio_goles (goals):
    
    return sum(goals)/25

def promedio_goles_jugador (jugadores):
        
    return max_goleador(jugadores)[1]/25