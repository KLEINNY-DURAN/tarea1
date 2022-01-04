#Para un valor entero positivo que representa una cantidad en segundos, indicar
#su equivalente en minutos, horas y días.
def run():
    segundos_kmdt = int(input("Ingrese los segundos:"))
    dia_kmdt = segundos_kmdt // 86400
    resto1_kmdt = segundos_kmdt % 86400
    horas_kmdt = resto1_kmdt // 3600
    resto2_kmdt = resto1_kmdt % 3600
    minutos_kmdt = resto2_kmdt // 60
    resto3_kmdt = resto2_kmdt % 60
    print("Son", dia_kmdt, "dia(s),", horas_kmdt, "horas,",minutos_kmdt, "minutos",resto3_kmdt, "segundos en total")

if __name__ == "__main__":
    run()