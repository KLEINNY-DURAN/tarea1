#Dado un (1) número binario de cuatro (4) dígitos imprimir su valor
def run():
    nbin_kmdt = input('Ingrese el número binario a convertir:')
    valor_kmdt = int(nbin_kmdt, 2)
    print('La conversión de binario a decimal es:', valor_kmdt)

if __name__ == "__main__":
    run()