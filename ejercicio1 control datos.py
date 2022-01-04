#Todos los años que se dividen exactamente entre 400, o que son divisibles
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
#Usando estas premisas crea un algoritmo que lea una fecha como un número
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
#el mismo es un año bisiesto o no.
def run():
    fecha_kmdt = int(input("Fecha en formato DDMMAAAA:"))
    año_kmdt = fecha_kmdt % 10000
    dia_kmdt = fecha_kmdt // 1000000
    mes_kmdt = (fecha_kmdt // 10000) % 100

    if año_kmdt % 4 != 0:
        print("El año",año_kmdt,"no es bisiesto")
    elif año_kmdt % 4 == 0 and año_kmdt % 100 != 0:
        print("El año",año_kmdt, "es bisiesto")

if __name__ == "__main__":
    run()