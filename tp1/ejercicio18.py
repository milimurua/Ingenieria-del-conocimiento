#2.18.	Procesamiento de ventas con arrays:
#Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array. Escribe una función que reciba el
#array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.
#   ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def procesar_ventas(sales):
    total = sum(float(sale) for sale in sales)
    average = total / len(sales)
    return total, average

daily_sales = [200, 450, 300, 400, 350, 500, 600]
total, average = procesar_ventas(daily_sales)
print(f"Total: {total}, Promedio: {average}")
