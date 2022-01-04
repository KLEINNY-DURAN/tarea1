#En un estacionamiento el monto a pagar se calcula multiplicando el número de
#horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
#incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
#Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
#y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
#calcule el monto a pagar por el dueño del vehículo.
#La entrada vendrá dada por dos enteros positivos el primero representa las horas
#y el segundo los minutos, además por último se debe leer un carácter (A o P) que
#indica si la hora es AM o PM.
horas_e_kmdt = int(input("Ingrese las horas en formato de 12 en la que se estaciono:"))
if horas_e_kmdt >= 0 and horas_e_kmdt <= 12:   
    min_e_kmdt = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if min_e_kmdt >= 0 and min_e_kmdt < 60: 
        am_pm_e_kmdt  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if am_pm_e_kmdt == "A" or am_pm_e_kmdt == "P" :
            horas_s_kmdt = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if horas_s_kmdt >= 0 and horas_s_kmdt <= 12:
                s_s_kmdt= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if s_s_kmdt >= 0 and s_s_kmdt < 60:
                    am_pm_sale_kmdt = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if am_pm_sale_kmdt == "A" or am_pm_sale_kmdt == "P" :
                        if am_pm_e_kmdt == "A" and am_pm_sale_kmdt == "A" or am_pm_e_kmdt == "A" and am_pm_sale_kmdt == "P" or am_pm_e_kmdt == "P" and am_pm_sale_kmdt == "P":
                            if am_pm_e_kmdt == "A" and am_pm_sale_kmdt == "A" or am_pm_e_kmdt == "P" and am_pm_sale_kmdt == "P":
                                res_H_kmdt = horas_e_kmdt - horas_s_kmdt
                                T_Horas_kmdt = res_H_kmdt * 4
                                res_M_kmdt = min_e_kmdt - s_s_kmdt
                                T_Min_kmdt = res_M_kmdt/30
                                T_Min_2_kmdt = 0
                                if T_Min_kmdt < 0 :
                                    T_Min_2_kmdt = 2.50
                                    T_Tiempo_kmdt = T_Horas_kmdt + T_Min_2_kmdt
                                    print("El Valor a pagar es: Bs", T_Tiempo_kmdt)
                            elif am_pm_e_kmdt == "A" and am_pm_sale_kmdt == "P":
                                horas_s_kmdt+=12
                                rest_Horas_kmdt = horas_e_kmdt - horas_s_kmdt
                                Total_Horas_kmdt = rest_Horas_kmdt * 4
                                rest_min_kmdt = min_e_kmdt - s_s_kmdt
                                Total_Min_kmdt = rest_min_kmdt/3
                                Total_Min_2_kmdt = 0
                                if Total_Min_kmdt < 0 :
                                    Total_Min_2_kmdt = 2.50
                                    Total_Tiempo_kmdt = Total_Horas_kmdt + Total_Min_2_kmdt
                                    print("El Valor a pagar es: Bs", Total_Tiempo_kmdt)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

