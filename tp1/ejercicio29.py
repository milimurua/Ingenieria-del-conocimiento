#2.29.	Registro de notas con tuplas y arrays:
# Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante
# y sus calificaciones en un array. La función debe devolver un diccionario con el nombre del estudiante como clave
# y su promedio de calificaciones como valor.
#   notas_estudiantes = [
#       ("Ana", [85, 90, 78]),
#       ("Luis", [88, 92, 80]),
#       ("María", [75, 85, 70])
#   ]
def students_avg_marks(students_marks):
    student_avg = {}
    for student, marks in students_marks:
        student_avg[student] = round(sum(marks) / len(marks))
    return student_avg


students_marks = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

print(students_marks)
print(students_avg_marks(students_marks))
