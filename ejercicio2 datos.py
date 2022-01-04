#¿Siguiendo la prioridad de operadores, convierta a expresión matemática,
#resuelva e indique en cuál tipo de variable almacenará el resultado de las
#siguientes expresiones:
#(5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
# 2 (4 – 10 + 8)/2*36 *(1/2)
# 260 / 12 + 54 % 3 – 85 % 7
# (48 < 2 * 3) | | (2 * 7 < 12)
# ((8 > 2) | | (932 < 23) ) && 4 == 2
print("""
    a)(5 + 3 * 2) + 9 > 3 * 5 * 14 % 3      
    b)2 (4 - 10 + 8)/2 36 *(1/2)    
    c)260 / 12 + 54 % 3 - 85 % 7  
    d)(48 < 2 * 3) | | (2 * 7 < 12)         
    e)((8 > 2) | | (932 < 23) ) && 4 == 2
     """)
opcion_kmdt = input("-Elija una opcion :")
if opcion_kmdt=="a":
    print("El resultado de esta operacion es 20>0 y cumpliendo su funcion se determina que es verdadera y es de tipo boolena " )
elif opcion_kmdt=="b":
    print("El resultado de esta operacion es 36 y es un dato entero (int)")
elif opcion_kmdt=="c":
    print("El resultado de esta operacion es 60,66 y es un dato decimal (float)")
elif opcion_kmdt=="d":
    print("El tipo de datos de esta ecuacion se determina FALSA y es de tipo booleana")
elif opcion_kmdt=="e":
    print("El tipo de datos de esta ecuacion se determina FALSA y es de tipo booleana")
else:
    print("Opción no válida, por favor seleccione una opcion correcta")