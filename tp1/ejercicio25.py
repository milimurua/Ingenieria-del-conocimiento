#2.25.	Análisis financiero con **kwargs:
# Consigna: Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs
# y calcule el balance final. La función debe manejar ingresos como positivos y gastos como negativos.
#   analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)

def balance_summary(**data):
    balance = 0
    for financial_element in data.values():
        balance += financial_element
    return balance

print("Balance final:",balance_summary(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500))

