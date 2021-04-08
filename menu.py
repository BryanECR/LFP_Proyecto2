def menu():
    while(True):
        opciones = '''
        ********************* Menu **************************
        *                                                   *
        *  1. Cargar Archivo                                *
        *  2. Mostrar información general de la gramática   *
        *  3. Generar autómata de pila equivalente          *
        *  4. Reporte de recorrido                          *
        *  5. Reporte en tabla                              *
        *  6. Salir                                         *
        *                                                   *
        *****************************************************
        '''
        print(opciones)
        op = input("Ingrese la opcion que desea")
        if op == 1:
            print("opcion 1")
        elif op == 2:
            print("opcion 2")
        elif op == 3:
            print("opcion 3")
        elif op == 4:
            print("opcion 4")
        elif op == 5:
            print("opcion 5")
        elif op == 6:
            print("\nHasta la Proxima\n")
            break
        else:
            print("Opcion no Valida ingrese un numero del 1 al 6")