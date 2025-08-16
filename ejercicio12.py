#2.12.	Gestión de inventario con tuplas:
# Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible.
# Representa cada producto como una tupla (nombre, precio, cantidad). Escribe una función que reciba una lista de
# productos (tuplas) y devuelva el producto más caro.
#
# productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]
products = []
create_product = 's'

while create_product == 's':
    name = input("name: ")
    price = float(input("price: "))
    quantity = input("quantity: ")

    product = (name, price, quantity)
    products.append(product) #agregar la tupla de productos a una lista

    create_product = input("¿Quieres llenar otro producto? [s/n]: ")

print("lista de productos: ", products)

max_product = max(products, key=lambda p: p[1]) # recorre products y cada p es un producto, compara para encontrar el precio más alto

print(max_product)
