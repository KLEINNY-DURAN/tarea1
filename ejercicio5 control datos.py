#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
#mayor? y ¿cuál es el segundo mayor?
def run():
    print("Ingrese tres números enteros positivos")
    A_kmdt = int(input("A: "))
    B_kmdt = int(input("B: "))
    C_kmdt = int(input("C: "))

    if A_kmdt > B_kmdt and A_kmdt > C_kmdt:
        print(A_kmdt, "es el número mayor")
        if B_kmdt > C_kmdt:
            print (B_kmdt, "es el segundo número mayor")
        else:
            print(C_kmdt, "es el segundo número mayor")
    elif B_kmdt > A_kmdt and B_kmdt > C_kmdt:
        print(B_kmdt, "es el número mayor")
        if A_kmdt > C_kmdt:
            print (A_kmdt,"es el segundo número mayor")
        else:
            print(C_kmdt,"es el segundo número mayor")
    elif C_kmdt > A_kmdt and C_kmdt > B_kmdt:
        print(C_kmdt, "es el número mayor")
        if A_kmdt > B_kmdt:
            print (A_kmdt, "es el segundo número mayor")
        else:
            print (B_kmdt, "es el segundo número mayor")
    else:
        print ("No se puede determinar")

if __name__ == "__main__":
    run()
