#¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
# “Hola Mundo"
# Verdadero
# „1'
# „c'
# 256
# 8>19
#proceso
print("""
    1)“Hola Mundo"       3)„1'       5)256
    2)Verdadero       4)„c'          6)8>19
     """)
opcion_kmdt = input("-Elija una opcion :")
if opcion_kmdt=="1":
    print("El tipo de dato (Hola mundo) es de tipo de dato STRING")
elif opcion_kmdt=="2":
    print("El tipo de datos de Verdadero es de tipo booleano")
elif opcion_kmdt=="3":
    print("El tipo de datos de ,1 es de tipo de dato decimal (float)")
elif opcion_kmdt=="4":
    print("El tipo de datos de ,c es de tipo Caracter (chr)")
elif opcion_kmdt=="5":
    print("El tipo de datos de 256 es de tipo entero (int)")
elif opcion_kmdt=="6":
    print("El tipo de datos de (8>19) es FALSO y es de tipo booleano")
else:
    print("Opción no válida, por favor seleccione una opcion corecta")