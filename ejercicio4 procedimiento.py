#En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
#cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
#incrementa en un 35% para las horas extras. Escribe una acción principal que
#solicite la identificación de 5 empleados, el monto cancelado por hora, y la
#cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
#calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
#concepto de horas extras, y finalmente informe los resultados en la acción
#principal.
def ejercicio4ayf (self):
        print("\n")
        empleados_kmdt = int(input("¿Cuántos empleados se identificaran? "))
        for i in range(empleados_kmdt):
            print("\n")
            name_kmdt = input("Identifiquese con sus nombres y apellidos: ")
            pagohora_kmdt = int(input("Ingrese el valor cancelado por hora: "))
            horastrabajadas_kmdt = int(input("Ingrese la cantidad de horas trabajadas: "))
            extrahoras_kmdt = int(input("Ingrese la cantidad de horas extras trabajadas: "))
            if horastrabajadas_kmdt > 40:
                tarifaextra_kmdt = pagohora_kmdt * (35 / 100)
                valorextra_kmdt = extrahoras_kmdt * tarifaextra_kmdt
                print("La cantidad ganada por las horas extras es", valorextra_kmdt)
                salariosemanal_kmdt = pagohora_kmdt * (horastrabajadas_kmdt - extrahoras_kmdt)
                print("El salario semanal es de", salariosemanal_kmdt)
                valorfinal_kmdt = salariosemanal_kmdt + valorextra_kmdt
                print("El valor final a cancelar por horas extras de", name_kmdt ,"es de", valorfinal_kmdt)
            else:
                salariosemanal_kmdt = pagohora_kmdt * (horastrabajadas_kmdt - extrahoras_kmdt)
                print("El salario semanal y final de" , name_kmdt, "es de", salariosemanal_kmdt)