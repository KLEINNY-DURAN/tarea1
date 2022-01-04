#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
#dicho número.
def run():
    num_kmdt = int(input("Ingrese un número: "))
    contador_kmdt = len(str(num_kmdt))
    print("El numero ingresado tiene %s digitos" % (contador_kmdt))

if __name__ == "__main__":
    run()