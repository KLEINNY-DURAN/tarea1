#Construya un programa que dado un valor entero N, haga el cálculo de la función
#factorial utilizando estructuras iterativas.
def run():
    num_kmdt = int(input('Ingresa un número: '))
    factorial_kmdt = 1
    if num_kmdt!=0:
        for i in range(1, num_kmdt + 1):
            factorial_kmdt = factorial_kmdt*i
    print("Factorial:", factorial_kmdt)
if __name__ == "__main__":
    run()