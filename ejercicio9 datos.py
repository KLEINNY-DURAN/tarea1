#Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
#decenas, centenas y unidades de mil.
#Entrada:
#1234
#Salida:
#Unidades: 4
#Decenas: 3
#Centenas: 2
#Unidades de mil: 1
def run():
    num_kmdt = int(input("Ingrese un número: \n"))
    n_kmdt = str(num_kmdt)
    print("Entrada:\n", num_kmdt)
    print("Salida:")
    print("Unidades {}".format(n_kmdt[3]))
    print("Decenas {}".format(n_kmdt[2]))
    print("Centenas {}".format(n_kmdt[1]))
    print("Unidades de mil {}".format(n_kmdt[0]))

if __name__ == "__main__":
    run()