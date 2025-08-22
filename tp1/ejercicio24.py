#2.24.	Organización de eventos con *args:
# Consigna: Escribe una función que reciba un número variable de nombres de eventos y los imprima
# en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.
# organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

def event_organizer(*events):
    for i, event in enumerate(events, start=1):
        print(f"{i}. {event}")


event_organizer("Concierto", "Exposición de arte", "Conferencia")
