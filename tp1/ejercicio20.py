#2.20.	Configuración de una aplicación con **kwargs:
#Consigna: Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro,
#idioma, notificaciones, etc., usando **kwargs. La función debe devolver un diccionario con las
#configuraciones aplicadas.
#   configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

def configure_app(**options):
    config = {
        "dark_mode": False,
        "language": "en",
        "notifications": True,
        "font_sizw": 14,
        "auto_update": True,
    }

    config.update(options)
    return config


print(configure_app(dark_mode=True, language="es", notifications=False))
print(configure_app(auto_update=False)) #other example

