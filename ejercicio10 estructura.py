#Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
#la serie termina al leer un 0.
def ejercicio10ei (self):
        print("\n")
        contador_kmdt = 0
        suma_kmdt = 0
        num_kmdt = int(input("Ingrese un número: "))
        while num_kmdt > 1:
            num_kmdt = int(input('Ingrese un número entero (0 para terminar): '))
            suma_kmdt += num_kmdt
            contador_kmdt += 1
            if contador_kmdt == 0:
                print('No ingreso ningun número: ')
            else:
                promedio_kmdt = suma_kmdt / contador_kmdt
        print('El promedio de los {} numeros es igual a {}.'.format(contador_kmdt, promedio_kmdt))