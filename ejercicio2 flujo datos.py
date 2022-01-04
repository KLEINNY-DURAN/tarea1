#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es
#capicúa.
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
def run():
    num_kmdt = int(input('Ingresa el valor de un número: '))
    if num_kmdt > 9999 and num_kmdt <= 99999:
        mil_kmdt = num_kmdt // 10000
        unidades_kmdt = num_kmdt % 10
        if mil_kmdt == unidades_kmdt:
            print("Es número capicúa")
        else:
            print("No es un número capicúa")
    else:
        print("No es un número con cinco dígitos")

if __name__ == "__main__":
    run()