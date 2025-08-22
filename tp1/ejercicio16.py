#2.16. Creación de un perfil de usuario con **kwargs:
# Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico,
# y cualquier otro dato adicional usando **kwargs. La función debe devolver un diccionario con toda la
# información del usuario.
#   crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

def create_user(*, name, age, email, city, **extras):
        return {
            "name": name,
            "age": int(age),
            "email": email,
            "city": city,
            **extras
        }

print("Nuevo usuario:", create_user(name="Luis", age=25, email="juan@mail.com", city = "Mendoza", lastname="Gomez"))