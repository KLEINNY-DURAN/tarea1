#Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
#peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
#base en dicha secuencia se desea realizar un estudio a fin de conocer:
# Edad promedio de todas las personas en la muestra.
# Peso promedio de todas las personas en la muestra.
# Estatura promedio de todas las personas en la muestra.
# Cuántas personas hay con edad entre los 18 y 25 años.
# Cuántas personas son mayores a 36 años.
# Cuál es el promedio de peso de las personas con edades entre 18 y 35
#años.     
def ejercicio7ei(self):
        print("\n")
        edad_kmdt=[20,30,40,50,60,70]
        peso_kmdt=[40,50,60,70,80,90]
        estatura_kmdt=[1.40,1.50,1.60,1.70,1.80,1.90]
        prom_edad_kmdt=(sum(edad_kmdt))/len(edad_kmdt)
        prom_peso_kmdt=(sum(peso_kmdt))/len(peso_kmdt)
        prom_estatura_kmdt=(sum(estatura_kmdt))/len(estatura_kmdt)
        c=0
        x=0
        while c < 8:
            x+=(edad_kmdt.count(20+c))
            c+=1  
        c=1
        cal_kmdt=0  
        while c<150:
            cal_kmdt+=(edad_kmdt.count(40+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad_kmdt) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso_kmdt[contPos[0+c]]
            c+=1
        print(contPos)
        print(f"El promedio de edades de todas las personas es de: {prom_edad_kmdt:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso_kmdt:.2f}")
        print(f"El promedio de estatura de todas las personas es de: {prom_estatura_kmdt:.2f}")
        print(f"Hay {x}, persona(s) con edad de entre [18-25] ")
        print(f"Hay {cal_kmdt}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")