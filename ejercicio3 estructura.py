#Dado un número N determinar si es un número primo.
#Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 
def run():
    num_kmdt= int(input("Ingresa un número: "))
    x_kmdt = 1
    cont_kmdt = 0
    while x_kmdt <= num_kmdt:
        if num_kmdt % x_kmdt == 0:
            cont_kmdt = cont_kmdt +1
        x_kmdt = x_kmdt + 1
    if cont_kmdt == 2:
        print ("Es un número primo")
    else:
        print ("No es un número primo")
if __name__ == "__main__":
    run()