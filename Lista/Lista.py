from Lista.Nodos import Nodo

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def incertar(self,nombre,terminales,noTerminales,inicial,producciones):
        if self.vacia():
            self.primero = self.ultimo =Nodo(nombre,terminales,noTerminales,inicial,producciones)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(nombre,terminales,noTerminales,inicial,producciones)
            self.ultimo.siguiente = self.primero

    def Buscar(self,buscar):
        aux = self.primero

        if self.vacia():
            print("No hay elementos en la lista")
        else:  
            while aux.siguiente != self.primero:
                if aux.nombre == buscar:
                    return aux
                aux = aux.siguiente

            if aux.nombre == buscar:
                    return aux 

            return "No Existe" 

    def imprimirLista(self):
        aux = self.primero

        if self.vacia():
            print("No hay elementos en la lista")
        else:  
            while aux.siguiente != self.primero:
                print("Nombre: "+str(aux.nombre))

                aux = aux.siguiente

            print("Nombre: "+str(aux.nombre))   
        