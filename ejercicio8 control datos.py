#Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
#2014 e imprima por pantalla el número de días que han pasado desde el 1 de
#Enero de 2014 hasta la fecha dada.
año_kmdt = int(input("Ingrese el año: "))
mes_kmdt = int(input("Ingrese el mes: "))
dia_kmdt = int(input("Ingrese el dia: "))
from datetime import date 
fechainicial_kmdt = date(2014,1,1) 
fechafinal_kmdt= date(año_kmdt,mes_kmdt,dia_kmdt) 
#calculo
dias_kmdt = fechafinal_kmdt - fechainicial_kmdt
print (dias_kmdt)
