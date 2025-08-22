#2.35.	Optimización de rutas con arrays y tuplas:
# Consigna: Una empresa de logística necesita optimizar sus rutas de entrega. Cada ruta se representa como una tupla
# (origen, destino, distancia). Escribe una función que reciba una lista de rutas y un array con las distancias
# máximas permitidas para cada ruta. La función debe devolver las rutas que cumplen con las restricciones.
#   rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
#   distancias_max = [600, 400, 500]

def route_optimization(routes, max_distances):
    return [r for i, r in enumerate(routes) if r[2] <= max_distances[i]]


routes = [
    ("Madrid", "Barcelona", 620),
    ("Madrid", "Valencia", 350),
    ("Barcelona", "Valencia", 350)
]
dis_max = [600, 400, 500]

print(dis_max)
print(route_optimization(routes, dis_max))
