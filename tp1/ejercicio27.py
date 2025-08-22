#2.27.	Estadísticas de ventas con arrays:
# Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario
# con el total de ventas, el promedio mensual, y el mes con mayores ventas.
#   ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
def sales_statics(sales):
    total_sales = sum(sales)

    return {
        "total": total_sales,
        "average": total_sales / len(sales),
        "maximum": max(sales)
    }


monthly_sales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
print(sales_statics(monthly_sales))
