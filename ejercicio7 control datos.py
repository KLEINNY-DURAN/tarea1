#El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
#cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
#del peso de una persona en relación con su altura.
#Clasificación del IMC de acuerdo con la OMS de la ONU:
#a. Menor a 16: Criterio de ingreso.
#b. 16 a 16.9: infra peso.
#c. 17 a 18.4: bajo peso.
#d. 18.5 a 24.9: peso normal.
#e. 25 a 29.9: sobrepeso.
#f. 30 a 34.9: obesidad pre-mórbida.
#g. 40 a 45: obesidad mórbida.
#h. Mayor a 45: obesidad híper-mórbida.
#Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
#centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
#de IMC de la persona y la categoría en la cual fue clasificado.
def ejercicio7fd (self):
        print("\n")
        peso_kmdt = int(input("Ingrese el peso de la persona en libras: "))
        estatura_kmdt = int(input("Ingrese la estatura en centímetros: "))
        kg_kmdt = peso_kmdt / (2.205)
        metro_kmdt = estatura_kmdt / 100
        imc_kmdt = kg_kmdt / (metro_kmdt*metro_kmdt)
        print("El IMC es de",imc_kmdt)
        if (imc_kmdt < 16):
            print("Criterio de ingreso")
        else:
            if (17 > imc_kmdt >= 16):
                print("Infra peso")
            else:
                if(18.4 >= imc_kmdt >= 17 ):
                    print ("Baja peso")
                else:
                    if(25 > imc_kmdt >= 18.5):
                        print("Peso normal")
                    else:
                        if(30 > imc_kmdt >= 25):
                            print("Sobrepeso")
                        else:
                            if ( 35 >  imc_kmdt >= 30):
                                print("Obesidad pre-mórbida")
                            else:
                                if (40 >= imc_kmdt >= 45):
                                    print("Obesidad mórbida")
                                else:
                                    if(imc_kmdt > 45):
                                        print("Obesidad hiper-mórbida")