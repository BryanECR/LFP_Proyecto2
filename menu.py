from Lectura import Lectura
import time

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
        op = int(input("\nIngrese la opcion que desea: "))
        if op == 1:
            Lectura.infoFile()

        elif op == 2:
            Lectura.imprimir()
            name = input("\nIngrese el nombre de la gramatica que desea visualizar: ")
            Lectura.imprimirInfo(name)

        elif op == 3:
            Lectura.imprimir()
            name = input("\nIngrese el nombre de la gramatica que desea Graficar: ")
            Lectura.grafica(name)
            
        elif op == 4:
            print("--------------- Gramaticas Disponibles ---------------")
            Lectura.imprimir()
            name = input("\nIngrese el nombre de la gramatica que desea valuar: ")
            palabra = str(input("Ingrese la palabra que desea valuar: "))
            Lectura.recorrido(palabra,name)
            
        elif op == 5:
            print("--------------- Gramaticas Disponibles ---------------")
            Lectura.imprimir()
            name = input("\nIngrese el nombre de la gramatica que desea valuar: ")
            palabra = str(input("Ingrese la palabra que desea valuar: "))
            Lectura.Tabla(palabra,name)

        elif op == 6:
            print("\nHasta la Proxima\n")
            break
        else:
            print("Opcion no Valida ingrese un numero del 1 al 6")

def cuenta():
    print("***** Proyecto 2 LFP *****\nNombre: Bryan Eduardo Caal Racanac\nCarnet: 201801155")
    numero = 5
    for i in range(numero):
        print(numero)
        time.sleep(1)
        numero-=1
        if(numero==0):
            print("¡Bienvenido!")
            menu()

cuenta()