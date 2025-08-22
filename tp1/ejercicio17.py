#2.17. Administración de empleados con tuplas y diccionarios:
#Consigna: Una empresa quiere administrar la información de sus empleados, donde cada empleado se
#representa como una tupla (nombre, edad, salario). Escribe una función que reciba un diccionario donde
#la clave es el ID del empleado y el valor es la tupla con su información. La función debe devolver un diccionario
#con los empleados que ganan más de un salario dado.
#   empleados = {
#       1: ("Ana", 30, 3000),
#       2: ("Luis", 25, 2500),
#       3: ("María", 35, 4000)
#   }

def show_higher_salaries(employees, min_salary):
    result = {}
    for employee_id, data in employees.items():
        name, age, salary = data  # data es una tupla (name, age, salary)
        if salary > min_salary:
            result[employee_id] = (name, age, salary)
    return result

employees = {}
id = 0

while True:
    id += 1
    name = input("Ingrese el nombre: ")
    age = int(input("Ingrese la edad: "))
    salary = float(input("Ingrese el salario: "))

    # Guarda como TUPlA (cumple consigna)
    employees[id] = (name, age, salary)

    continue_complete = input("¿Seguir agregando empleados? [s/n]: ").strip().lower()
    if continue_complete == 'n':
        break

print("Employees:", employees)
min_salary = float(input("Ingresar un salario: "))
print(show_higher_salaries(employees, min_salary))


