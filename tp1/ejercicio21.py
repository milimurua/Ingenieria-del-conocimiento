#2.21.	Ordenamiento de datos con tuplas:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre
# y una puntuación. La función debe devolver la lista ordenada por puntuación de mayor a menor.
#   puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

# 1) Creamos una lista vacía para guardar (nombre, puntuación)
def get_score(item):
    return item[1]
def sort_scores(scores):
    return sorted(scores, key=get_score, reverse=True)

scores = [("Ana", 85), ("Luis", 90), ("María", 78)]
print("Puntuaciones: ", scores)

sorted_scores = sort_scores(scores)
print("Puntuaciones ordenadas: ", sorted_scores)
