#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
#número.
def run():
    número_kmdt = int(input("Ingrese un número entre el 1 y el 12: "))
    if número_kmdt == 1:
        print("Enero")
    elif número_kmdt == 2:
        print("Febrero")
    elif número_kmdt == 3:
        print("Marzo")
    elif número_kmdt == 4:
        print("Abril")
    elif número_kmdt == 5:
        print("Mayo")
    elif número_kmdt == 6:
        print("Junio")
    elif número_kmdt == 7:
        print("Julio")
    elif número_kmdt == 8:
        print("Agosto")
    elif número_kmdt == 9:
        print("Septiembre")
    elif número_kmdt == 10:
        print("Octubre")
    elif número_kmdt == 11:
        print("Noviembre")
    elif número_kmdt == 12:
        print("Diciembre")
    else:
        print("No existe mes con ese número")

if __name__ == "__main__":
    run()