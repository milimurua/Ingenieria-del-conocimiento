#2.34.	Análisis de resultados de encuestas con diccionarios y arrays:
# Consigna: Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde la clave
# es la pregunta y el valor es un array con las respuestas recibidas. Escribe una función que calcule la frecuencia de
# cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.
#   encuestas = {
#       "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
#       "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
#   }


def poll_results(poll):
    result_repetitions = {}
    for question, answers in poll.items():
        counts = {resp: answers.count(resp) for resp in answers}
        result_repetitions[question] = counts
    return result_repetitions


surveys= {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
print(surveys)
print("resultados",poll_results(surveys))
