#2.19.	Análisis de resultados deportivos con diccionarios:
#Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde la
#clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos.
#Escribe una función que calcule el total de goles anotados y recibidos en la temporada.
#   resultados = {
#       "Equipo A": (3, 2),
#        "Equipo B": (1, 1),
#        "Equipo C": (4, 0)
#    }

def calculate_goals_favor(results):
    total_favor = 0
    for gf, gc in results.values():
        total_favor += gf
    return total_favor

def calculate_goals_received(results):
    total_received = 0
    for gf, gc in results.values():
        total_received += gc
    return total_received

results = {
    "Team A": (3, 2),
    "Team B": (1, 1),
    "Team C": (4, 0)
}

print("Total de goles a favor:", calculate_goals_favor(results))
print("Total de goles en contra:", calculate_goals_received(results))
