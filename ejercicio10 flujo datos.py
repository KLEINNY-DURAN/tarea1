#En un almacén se hace un 20% de descuento a los clientes cuya compra supere
#los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
#pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
#necesario.
def run():
    monto_kmdt = int(input("Ingrese el monto a cancelar para verificar si obtiene el descuento: "))
    if monto_kmdt > 1000:
        descuento1_kmdt = monto_kmdt * 0.20
        valorapagar_kmdt = monto_kmdt - descuento1_kmdt
        print ("El monto a cancelar es: ", valorapagar_kmdt)
        print("Nota: incluido descuento de 20%")
    else:
        print("El monto a cancelar es:", monto_kmdt)
        print("Nota: El monto a cancelar no incluye descuento")

if __name__ == "__main__":
    run()