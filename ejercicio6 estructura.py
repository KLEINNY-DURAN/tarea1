#Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
#informe al usuario qué valor tiene el número mayor y qué valor tiene el número
#menor, sin contar el cero (0).
def secuencia_menor_mayor():
    ingresa_kmdt = True
    lista_kmdt = []
    while ingresa_kmdt:
        valor_kmdt = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
        if valor_kmdt == 0:
            break
        else:
            lista_kmdt.append(valor_kmdt) 
    print(lista_kmdt)
    print(u'Menor %s' % min(lista_kmdt)) 
    menor_kmdt = lista_kmdt[0] 
    mayor_kmdt = lista_kmdt[0] 
    for elemento in lista_kmdt: 
        if elemento < menor_kmdt: 
            menor_kmdt = elemento
    for elemento in lista_kmdt:
        if elemento > mayor_kmdt:
            mayor_kmdt = elemento
    print(u'Menor %s' % menor_kmdt)
    print(u'Mayor %s ' % max(lista_kmdt))
    print(u'Mayor %s ' % mayor_kmdt)
