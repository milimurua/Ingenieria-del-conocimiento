#2.33.	Sistema de reservas con tuplas y diccionarios:
# Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es una
# lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. Escribe una función
# que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.
#   reservas = {
#       "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
#       "2024-08-16": [("Luis", 101, 150)]
#   }

def hotel_booking(books, new_book, date):
    if date in books:
        for book in books[date]:
            if book[1] == new_book[1]:
                print("La habitación ya está reservada en esa fecha.")
                return books
        books[date].append(new_book)
    else:
        books[date] = [new_book]

    return books

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
fecha_usuario = input("Ingrese la fecha de la reserva (formato YYYY-MM-DD): ")
nueva_reserva = ("Pedro", 102, 200)
resultado = hotel_booking(reservas, nueva_reserva, fecha_usuario)
print(resultado)