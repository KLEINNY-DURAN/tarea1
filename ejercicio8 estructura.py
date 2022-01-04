#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
#del 1 hasta la del 10.
def run():
    num_kmdt = int(input("Introduzca el número de la tabla que desee: "))
    for i in range(0,11):
        resul_kmdt = i * num_kmdt
        print(num_kmdt, "x", i, "=", resul_kmdt)
if __name__ == "__main__":
    run()