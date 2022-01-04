#Construya una función que solicite edades al usuario y determine el promedio de
#las edades mayores a 18 años. El usuario indicará cuando desea dejar de
#suministrar datos de entrada. En la Acción Principal se informará el promedio
#calculado.
def ejercicio1ayf (self):
        print("\n")
        print("\tProcedimientos (Acciones y Funciones)")
        print("\n")
        acumulador_kmdt = 0
        nedad_kmdt = int(input("Ingrese cuantas edades se ingresará: "))
        for i in range(nedad_kmdt):
            edad_kmdt = int(input("Ingrese la edad, nota: las edades deben ser mayores a 18: "))
            if edad_kmdt >= 18:
                acumulador_kmdt = acumulador_kmdt + edad_kmdt
                promedio_kmdt = acumulador_kmdt / nedad_kmdt
        print("El promedio de las edades es de", promedio_kmdt)