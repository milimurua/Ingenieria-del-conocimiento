#2.13.	Registro de estudiantes con diccionarios:
# Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un
# diccionario con nombre, edad y calificaciones en distintas materias. Escribe una función que reciba el registro de
# estudiantes y devuelva el promedio de calificaciones de un estudiante dado su número de matrícula.

#estudiantes = {
#    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
#    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
#}

def calculate_average(id, students):
    if id not in students:
        print("no existe ese id")
        return None
    average = 0.0
    counter = 0
    calif = students[id]["ratings"]

    for mark in calif.values():
        average += float(mark)
        counter +=1
    return average / counter

students = { }
id = 0

while True:
    id += 1
    name = input("ingrese el nombre: ")
    age = int(input("ingrese la edad: "))

    ratings = {}
    print("introducir las calificaciones: ")
    while True:
        curse = input("Materia: ")
        mark = float(input("Ingrese la nota: "))
        ratings[curse] = mark

        continue_ratings = input("Seguir agregando materias? [s/n]: ")
        if continue_ratings == 'n':
            break

    students[id] = {
        "name" : name,
        "age": age,
        "ratings": ratings
    }

    continue_complete = input("Seguir agregando estudiantes? [s/n]: ")
    if continue_complete == 'n':
        break


print("Estudiantes: ", students)
id_student = int(input("Ingresa el id del estudiante: "))
prom = calculate_average(id_student, students)
print(f'Promedio de {id_student} es: {prom}')