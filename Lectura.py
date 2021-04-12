from tkinter import filedialog
from Lista.Lista import Lista
import os

lista = Lista()

class Lectura:

    def analizarGramaticas(cadena):
        producciones = str(cadena).replace("*","").split("\n")
        
        tamañoProducciones = []
        for i in range(len(producciones)):
            a = str(producciones[i]).replace(" ","").split("->")
            if len(a) != 1:
                tamañoProducciones.append(len(a[1]))
            
        aux = 0
        for i in range(len(tamañoProducciones)):
            
            if tamañoProducciones[i] > aux:
                aux = tamañoProducciones[i]
                
        return aux
        
    def convetTuple(tup):
        cadena = ''.join(tup)
        return cadena

    def abrirArchivo():
       file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.*"),("all files", "*.*")) )
        
       return file_path

    def infoFile():
        ruta = Lectura.abrirArchivo()
        file = open(ruta,"r")
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
            nombre = elementos[0]
            c = elementos[1].split(";")
            contador = 2
            cadena2 = ""
            while( contador < len(elementos) ):
                cadena2 += "\n"+str(elementos[contador]) 
                contador +=1
            
            gramatica = Lectura.analizarGramaticas(cadena2)

            if gramatica >= 3:
                lista.incertar(nombre,c[1],str(c[0]),str(c[2]),cadena2)

        print("\n********** Archivo abierto Correctamente **********\n")
    
    #LISTA DE LAS GRAMATICAS GUARDADAS
    def imprimir():
        lista.imprimirLista()

    #DATOS DE LA LISTA A ELEGIR
    def imprimirInfo(name):
        datos = lista.buscar(name)

        print("Nombre: "+Lectura.convetTuple(datos.nombre)+"\nNo Terminales = {"+Lectura.convetTuple(datos.noTerminales)+"} \nTerminales={"+Lectura.convetTuple(datos.terminales)+"} \nInicial={"+str(datos.inicial)+"} \nProduccion: "+str(datos.producciones).replace(" ","|"))

    def reporte(imagen):
        cadena = '''
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>CFG</title>
        <style>
        html {
        height: 100%;
        /* max-height: 600px; */
        width: 1000px;
        background-color: hsla(200,40%,30%,.4);
        background-image:		
        url('https://78.media.tumblr.com/cae86e76225a25b17332dfc9cf8b1121/tumblr_p7n8kqHMuD1uy4lhuo1_540.png'), 
        url('https://78.media.tumblr.com/66445d34fe560351d474af69ef3f2fb0/tumblr_p7n908E1Jb1uy4lhuo1_1280.png'),
        url('https://78.media.tumblr.com/8cd0a12b7d9d5ba2c7d26f42c25de99f/tumblr_p7n8kqHMuD1uy4lhuo2_1280.png'),
        url('https://78.media.tumblr.com/5ecb41b654f4e8878f59445b948ede50/tumblr_p7n8on19cV1uy4lhuo1_1280.png'),
        url('https://78.media.tumblr.com/28bd9a2522fbf8981d680317ccbf4282/tumblr_p7n8kqHMuD1uy4lhuo3_1280.png');
        background-repeat: repeat-x;
        background-position: 
        0 20%,
        0 100%,
        0 50%,
        0 100%,
        0 0;
        background-size: 
        2500px,
        800px,
        500px 200px,
        1000px,
        400px 260px;
        animation: 50s para infinite linear;
        }
        @keyframes para {
        100% {
        background-position: 
        -5000px 20%,
        -800px 95%,
        500px 50%,
        1000px 100%,
        400px 0;
        }
        }
        .imagen{
        align-content: center;
        width: 70%;
        margin-left: 150px;
        margin-top: 50px;
        padding: 5%;
        background-color: azure;
        }      
        </style>
        </head>
        <body>
        '''
        cadena += '<img class="imagen" src="'+imagen+'">'
        cadena +='''
        </body>
        </html>
        '''

        file = open("reporte.html","w")
        file.write(cadena)
        file.close()
        os.system("reporte.html")

    #GENERAR GRAFICA DE LA GRAMATICA EN GRAPHVIZ Y METERLA EN UN HTML
    def grafica(name):
        info = lista.buscar(name)
        terminales = Lectura.convetTuple(info.terminales)
        inicial = info.inicial
        adp = terminales+","+Lectura.convetTuple(info.noTerminales)+",#"

        cadena = 'x[label = "Nombre: AP_'+str(name)+'\nTerminales = {'+terminales+'}\nAlfabeto de pila = {'+adp+'} \nEstados = {'+"i,p,q,f"+'}\nEstado Inicial = {'+"i"+'}\nEstado de Aceptacion = {'+"f"+'}",shape=square ]\nrankdir=LR;\nnode [shape = doublecircle]; f;\nnode [shape = circle]; \ni -> p [label = "$,$;#"]'
        cadena += '\np -> q [label="$,$;'+inicial+'"]\nq -> q [ label = "'
        
        #Producciones
        produ = str(info.producciones).replace("*","").replace(" ",",").replace("->",";").strip().split("\n")
        for i in range(len(produ)):
            cadena += '$,'+str(produ[i])+'\n'
        
        #No Terminales
        tr = list(terminales)
        for i in range(len(tr)):
            if str(tr[i]) != ",":
                cadena += str(tr[i])+","+str(tr[i])+",$\n"
        
        cadena+='"]\nq -> f [label = "$,#,$"]'

        file = open(str(name)+".dot","w")
        file.write("digraph G {\n"+cadena+"\n}")
        file.close()
        os.system('dot -Tpng '+str(name)+'.dot -o '+str(name)+'.png')
        Lectura.reporte(str(name)+'.png')
