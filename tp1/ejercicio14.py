#2.14.	Análisis de datos meteorológicos con arrays:
# Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array.
# Escribe una función que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.
#   temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

temperatures = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def calculate_average_temperature(temperatures):
    total = 0.0
    counter = 0
    for temperature in temperatures:
        total += temperature
        counter += 1
    return total / counter

def calculate_max_temperature(temperatures):
    return max(temperatures)

def calculate_min_temperature(temperatures):
    return min(temperatures)

def temperature_menu():
    while True:
        option = int(input(
            "Selecciona una opción:\n"
            "1. Calcular temperatura media\n"
            "2. Calcular temperatura máxima\n"
            "3. Calcular temperatura mínima\n"
            "4. Salir\n"
            "Opción: "
        ))

        if option == 1:
            print("Temperatura media:", calculate_average_temperature(temperatures), "\n")
        elif option == 2:
            print("Temperatura máxima:", calculate_max_temperature(temperatures), "\n")
        elif option == 3:
            print("Temperatura mínima:", calculate_min_temperature(temperatures), "\n")
        elif option == 4:
            break
        else:
            print("Opción inválida\n")

temperature_menu()
