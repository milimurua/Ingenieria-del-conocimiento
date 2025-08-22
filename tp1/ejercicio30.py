#2.30.	Configuración de perfiles de usuario con **kwargs y arrays:
# Consigna: Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs.
# La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las
# configuraciones aplicadas.
#   usuarios = ["Ana", "Luis", "María"]
#   configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
def user_settings(users, **settings):
    applied_settings = {}
    for user in users:
        applied_settings[user] = settings.copy()
    return applied_settings


users = ["Ana", "Luis", "María"]
print(user_settings(users, idioma="es", modo_oscuro=True, notificaciones=False))
