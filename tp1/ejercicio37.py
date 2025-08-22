#2.37.	Análisis de tendencias en redes sociales con arrays y tuplas:
# Consigna: Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales.
# Escribe una función que reciba un array de hashtags y una lista de tuplas donde cada tupla contiene un hashtag y
# su frecuencia de uso. La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad
# de veces.
#   hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
#   tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def trend_analysis(hashtags, trends, min_usage):
    hashtags_set = set(hashtags)
    return [tag for tag, freq in trends if tag in hashtags_set and freq >= min_usage]


hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
trends = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

print(trend_analysis(hashtags, trends, 100))