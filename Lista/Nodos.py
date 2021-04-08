class Nodo:
    def __init__(self,nombre,terminales,noTerminales,inicial,producciones):
        self.nombre = nombre,
        self.terminales = terminales,
        self.noTerminales = noTerminales,
        self.inicial = inicial
        self.producciones = producciones
        self.siguiente = None