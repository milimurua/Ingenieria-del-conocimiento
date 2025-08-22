#2.40.	Análisis de rendimiento académico con diccionarios y arrays:
# Consigna: Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias.
# Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor
# es otro diccionario con las materias y sus respectivas calificaciones (arrays). Escribe una función que reciba este
# diccionario y devuelva un ranking de estudiantes basado en su promedio general.
#   estudiantes = {
#       101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
#       102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
#       103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
#   }
def students_ranking(students):
    averages = {}

    for student_id, subjects in students.items():
        total = 0
        count = 0
        for grades in subjects.values():
            total += sum(grades)
            count += len(grades)
        averages[student_id] = total / count

    ranking = sorted(averages, key=averages.get, reverse=True)

    return ranking

students = {
    101: {"math": [85, 90, 78], "science": [88, 85, 80]},
    102: {"math": [92, 88, 84], "science": [75, 80, 85]},
    103: {"math": [78, 85, 88], "science": [90, 95, 92]}
}

print("Ranking de promedios: ", students_ranking(students))

