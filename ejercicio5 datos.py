#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
dato1_kmdt = int(input("Ingrese dato del cateto a:  "))
dato2_kmdt = int(input("Ingrese dato del cateto b:  "))
#calculo
import math
valorraiz_kmdt = (dato1_kmdt * 2) + (dato2_kmdt* 2)
hipotenusa_kmdt = math.sqrt(valorraiz_kmdt)
print("El resultado de la hipotenusa es: "+str(hipotenusa_kmdt))