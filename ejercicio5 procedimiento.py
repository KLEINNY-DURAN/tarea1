#Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
#kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
#de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
#ellas y debe retornar la distancia entre las ciudades en kilómetros.
#Desarrolle además una acción principal en donde utilice a la acción
#MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
#de ciudades suministradas por el usuario.
#Entrada:
#Cuidad A
#Ciudad B
#332
#Salida:
#Entre la Ciudad A y la Ciudad B hay 534.30 Km.
def ejercicio5ayf (self):
        print("\n")
        acumulador_kmdt = 0
        for i in range (4):
            ciudada_kmdt = input("Ingrese el nombre de la ciudad de origen: ")
            ciudadb_kmdt = input("Ingrese el nombre de la ciudad de destino: ")
            distancia_kmdt = int(input("Ingrese la distancia en millas que hay entre las dos ciudades: "))
            km_kmdt = distancia_kmdt * (1.60935)
            print("La distancia en km que hay entre", ciudada_kmdt, "y", ciudadb_kmdt, "es de", km_kmdt, "km")
            acumulador_kmdt = acumulador_kmdt + km_kmdt
        print("La suma de distancia entre los 4 pares de ciudades es", acumulador_kmdt)