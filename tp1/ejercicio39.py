#2.39.	Simulación de mercado bursátil con arrays y tuplas:
# Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil. La función debe
# recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y un
# precio de compra o venta. La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado
# y vendido en los días especificados.
#   precios_diarios = [100, 105, 102, 110, 108]
#   operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
def market_simulation(prices, operations):
    balance = 0
    for action, day in operations:
        price = prices[day]
        if action == "venta":
            balance += price
        elif action == "compra":
            balance -= price
    return balance


precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

print(market_simulation(precios_diarios, operaciones))