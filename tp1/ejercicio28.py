#2.28.	Organización de una biblioteca con diccionarios:
# Consigna: Una biblioteca registra sus libros en un diccionario donde la clave es el título del libro
# y el valor es otro diccionario con la información del autor, año de publicación, y género. Escribe una
# función que reciba este diccionario y devuelva una lista de todos los libros publicados después del año 2000.
#   biblioteca = {
#       "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
#       "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
#       "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
#   }
def sort_library(books, min_year):
    return [title for title, info in books.items() if info["año"] > min_year]


biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

# pedir al usuario el año
anio_usuario = int(input("Ingrese un año para filtrar los libros: "))

# mostrar resultado
resultado = sort_library(biblioteca, anio_usuario)
print("Libros publicados después de", anio_usuario, ":", resultado)
