#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
#resultado su equivalente en segundos.
def run():
    horas_kmdt = int(input("Ingrese las horas:"))
    minutos_kmdt = int(input("Ingrese los minutos:"))
    s1_kmdt = horas_kmdt * 3600
    s2_kmdt = minutos_kmdt * 60
    segundos_kmdt = s1_kmdt + s2_kmdt
    print("En total hay", segundos_kmdt, "segundos")

if __name__ == "__main__":
    run()