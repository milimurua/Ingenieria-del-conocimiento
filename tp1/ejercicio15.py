#2.15. Manejo de parámetros variables con *args:
# Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio.
# Utiliza *args para recibir las notas.
#   calcular_promedio(85, 90, 78, 92)

def calculate_average(*students_notes):
    total = 0.0
    for note in students_notes:
        total += float(note)
    return total / len(students_notes)

def complete_notes(notes_list):
    while True:
        note = float(input("Agregar una nota: "))
        notes_list.append(note)

        option = input("¿Quieres seguir agregando notas? [s/n]: ").strip().lower()
        if option == 'n':
            break

students_notes = []
complete_notes(students_notes)
prom = calculate_average(*students_notes)
print("El promedio es:", prom)
