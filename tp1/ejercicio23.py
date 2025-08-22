#2.23.	Gestión de inventario con arrays:
# Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto
# específico y su valor es la cantidad disponible. Escribe una función que reciba el array de inventario y
# un número de productos vendidos (otro array) y devuelva el inventario actualizado.
#   inventario = [50, 30, 20, 10]
#   ventas = [5, 10, 5, 2]

def inventory_sync(inventory, sales):
    return [p - sales[inventory.index(p)] for p in inventory]


inventory = [50, 30, 20, 10]
sales = [5, 10, 5, 2]
print("Inventario inicial: ",inventory, "\nVentas: ",sales)
print("Inventario actual: ",inventory_sync(inventory, sales))
