#2.38.	Administración de suscripciones con diccionarios, arrays, y **kwargs:
# Consigna: Escribe una función que gestione las suscripciones a un servicio en línea. La función debe recibir
# el nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier o	tra opción adicional usando **kwargs.
# La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el
# estado actualizado.
#   suscripciones = {
#       "Jose": ["mensual", "anual"],
#       "Ana": ["mensual"]
#   }
#   actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)

subscriptions = {
    "Jose": ["monthly", "annual"],
    "Ana": ["monthly"]
}

def update_subscription(user, subscription, **options):
    if user in subscriptions:
        subscriptions[user].append(subscription)
    else:
        subscriptions[user] = [subscription]

    if options:
        print(f"Extra options for {user}: {options}")

    return subscriptions


print(update_subscription(user="Luis", subscription="monthly", auto_renew=True))