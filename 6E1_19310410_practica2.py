import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.anterior = None
        self.visitados = False
        self.peso = float('inf')

    def agrVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])
            

class Grafo:
    def __init__(self):
        
        self.vertices = {} #Se crea un diccionario donde más adelante se van a guardar objetos tipo Vertice

    def agrVertice(self,id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id) #Se guarda un objeto tipo vertice con su id correspondiente

    def agrArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agrVecino(b,p) #Agrega el vecino 'b' con el peso de la arista que los conecta en el diccionario con el id 'a'
            self.vertices[b].agrVecino(a,p)

    def recorrido(self, v):
        recorrido = []
        actual = v
        while actual != None:
            recorrido.insert(0, actual) #Insertamos en la lista del recorrido al inicio (0) el valor actual que es el id del vertice
            actual = self.vertices[actual].anterior #Actualizamos actual con el vertice anterior visitado
        return (recorrido, self.vertices[v].peso) #devuelve la lista recirrido y el peso de todo el recorrido

    def rec_min(self, lista): #recibe la lista de los vertices no visitados
        if len(lista)>0: #Revisa si aun hay vertices que visitar
            dis = self.vertices[lista[0]].peso
            v = lista[0]
            for e in lista:
                if dis < self.vertices[e].peso: #realiza comparaciones de los pesos de cada vértice en la lista para encontrar el de menor peso (distancia)
                    dis = self.vertices[e].peso
                    v = e
            
            return v

    def Dijkstra(self, a):
        if a in self.vertices: #Verificamos si el vertice que mandamos de entrada existe en 
            self.vertices[a].peso = 0 #Al peso del vertice inicial le ponemos cero ya que es nuestro punto de salida
            noVisit = [] #lista de vertices no visitados
            actual = a

            for v in self.vertices: # Recorremos todos los vertices en nuestro diccionario
                noVisit.append(v) # Y metemos todos los vertices a la lista de no visitados
            
            while len(noVisit) > 0: # Mientras nuestra lista de no visitados tenga elementos dentro:
                for vecino in self.vertices[actual].vecinos: # Recorre todos los vecinos de nuestro vertice actual
                    if self.vertices[vecino[0]].visitados == False: # vecino[0] nos da el id del vertice vecino de nuestro vertice actual, y ve si compara si ya se visitó
                        if self.vertices[actual].peso + vecino[1] < self.vertices[vecino[0]].peso: # Si el peso del vertice actual más la del vecino es menor que el peso del vecino en ese momento
                            self.vertices[vecino[0]].peso = self.vertices[actual].peso + vecino[1]
                            self.vertices[vecino[0]].anterior = actual #El vertice anterior/padre/predecesor del vecino en ese momento es el vertice actual

                self.vertices[actual].visitado = True #Marcamos como visitado el vertice actual
                noVisit.remove(actual) #Eliminamos de la lista de no visitados al vertice actual
                actual = self.rec_min(noVisit) #Seleccionamos al vertice con el menor peso y repetimos el proceso
            else:
                return False

g = Grafo()
g.agrVertice('A') 
g.agrVertice('B') 
g.agrVertice('C') 
g.agrVertice('D') 
g.agrVertice('E') 
g.agrArista('A', 'B', 6)
g.agrArista('A', 'C', 5)
g.agrArista('A', 'D', 8)
g.agrArista('B', 'C', 4)
g.agrArista('B', 'D', 5)
g.agrArista('B', 'E', 3)
g.agrArista('C', 'D', 6)
g.agrArista('D', 'E', 2)

print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
g.Dijkstra('C')
print(g.recorrido('E'))

G = nx.Graph([("A","B"),("A","C"),("A","D"),
                ("B","C"),("B","D"),
                ("B","E"),
                ("C","D"),("D","E")])
nx.draw(G,with_labels=True,font_color='white')
plt.show()
