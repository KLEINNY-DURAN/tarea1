#Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
from math import sqrt

num1_kmdt = int(input("Ingrese el primer número: \n"))
num2_kmdt = int(input("Ingrese el segundo número: \n"))
num3_kmdt = int(input("Ingrese el tercer número: \n"))
x1_kmdt = 0
x2_kmdt = 0

if ((num2_kmdt ** 2) - 4 * num1_kmdt * num3_kmdt) < 0:
        print("La solución de la ecuación es con números complejos")
else:
    x1_kmdt = (-num2_kmdt + sqrt(num2_kmdt ** 2 - (4 * num1_kmdt * num3_kmdt))) / (2 * num1_kmdt)
    x2_kmdt = (-num2_kmdt - sqrt(num2_kmdt ** 2 - (4 * num1_kmdt * num3_kmdt))) / (2 * num1_kmdt)
    print("Las soluciones son:")
    print("El valor de x1 es:",x1_kmdt)
    print("El valor de x2 es:",x2_kmdt)