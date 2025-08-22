#2.26.	Registro de empleados con tuplas y **kwargs:
# Consigna: Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros
# obligatorios, y otros datos como dirección, número de teléfono, etc., como **kwargs. La función debe devolver
# un diccionario con toda la información del empleado.
#   registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
def personal_data(name, age, salary, **other_data):
    return {"name": name, "age": age, "salary": salary, **other_data}


print(personal_data("Ana", 30, 3000, direccion="Calle Falsa 123", phone="123456789"))
