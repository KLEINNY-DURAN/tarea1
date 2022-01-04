#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit
#de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
lista_kmdt=[]
for x in range(4):
    valor_kmdt=int(input("Ingrese un valor entero: "))
    lista_kmdt.append(valor_kmdt)
repe_kmdt = lista_kmdt.count(1)
if repe_kmdt % 2 == 0:
    print("El codigo de paridad es 1 y es impar")
else:
    print("El codigo de paridad es 0 y es par")