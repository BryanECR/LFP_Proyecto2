from tkinter import filedialog
from Lista.Lista import Lista

lista = Lista()

class Lectura():
    def abrirArchivo():
       file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.*"),("all files", "*.*")) )
        
       return file_path


    def infoFile():
        file = open('entrada.txt',"r")
        c = file.readlines()
        file.close()

        #SEPARAR LAS GRAMATICAS DEL ARCHIVO
        numeroGramaticas = []
        cadena = ""
        for i in range(len(c)):
            cadena += c[i]
            if str(c[i]).strip() == "*":
                numeroGramaticas.append(cadena)
                cadena = ""

        #ORDENAR LOS DATOS QUE CONTIENEN LAS GRAMATICAS
        for i in range(len(numeroGramaticas)):
            elementos = str(numeroGramaticas[i]).split("\n")
            nombre = str(elementos[0])
            c = elementos[1].split(";")
            #print("Nombre: "+str(nombre)+"\nNo Terminales: "+c[0]+"\nTerminales: "+c[1]+"\nTerminal inicial: "+c[2]+"\nProducciones: " )
            contador = 2
            cadena = ""
            while( contador < len(elementos) ):
                #print(elementos[contador])
                cadena += "\n"+str(elementos[contador]) 
                contador +=1
            
            lista.incertar(nombre,str(c[1]),str(c[0]),str(c[2]),cadena)
    
    def imprimir():
        lista.imprimirLista()

    def buscar(nombre):
        datos = Lista.buscar(nombre)
        print("Nombre: "+str(datos.nombre)+"\nNo Terminales = {"+str(datos.noTerminales)+"} \nTerminales={"+str(datos.terminales)+"} \nInicial={"+str(datos.inicial)+"} \nProduccion="+str(datos.producciones))

        
Lectura.infoFile()
Lectura.imprimir()