#Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
#suma de los lados del polígono).
def ejercicio3ayf (self):
        print("\n")
        print("¿De que tipo de pentagono quiere calcular el perímetro?")
        penta_kmdt = int(input("Regular o irregular? /n Nota: Regular es 1 e Irregular es 0: "))
        if penta_kmdt == 1:
            lado_kmdt = int(input("Ingrese el valor de los lados del pentágono: "))
            perimetro_kmdt = lado_kmdt * 5
            print(str(lado_kmdt) + "+" + str(lado_kmdt) + "+" + str(lado_kmdt) + "+" + str(lado_kmdt) + "+" + str(lado_kmdt) + " es igual a:", perimetro_kmdt)
        else:
            lado1_kmdt = int(input("Ingrese el valor del primer lado del pentágono: "))
            lado2_kmdt = int(input("Ingrese el valor del segundo lado del pentágono: "))
            lado3_kmdt = int(input("Ingrese el valor del tercer lado del pentágono: "))
            lado4_kmdt = int(input("Ingrese el valor del cuarto lado del pentágono: "))
            lado5_kmdt = int(input("Ingrese el valor del quinto lado del pentágono: "))
            perimetro_kmdt = lado1_kmdt + lado2_kmdt + lado3_kmdt + lado4_kmdt + lado5_kmdt
            print("El perímetro del pentágono es", perimetro_kmdt)