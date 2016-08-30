# Directed/Undirected Graphs
# Adjacency List
# This implementation also works for weighted graphs.

class Vertex(object):

    def __init__ (self,key):
        self.id = key
        self.connections = {}

    def addNeighbor(self,nbr,weight=0):
        self.connections[nbr] = weight
        return True

    def getConnections(self):
        return self.connections.keys()

    def getId(self):
        return self.id

    def getWeight(self):
        return self.weight

    def getDegree(self):
        return len(self.connections)

    def __structure__(self):
        return str(self.id)+ ' connected to: ' + str([x for x in self.connections.keys()])

class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.graph_size = 0

    def addVertex(self,key):
        if key not in self.vetices.keys():
            self.vertices[key] = Vertex(key)
            self.graph_size += 1
            return True
        return False

    def getVertex(self,key):
        if key in self.vertices.keys():
            return self.vertices[key]
        else:
            raise KeyError('%s does not exist' % key)

    def addEdge(self,front_key,tail_key,weight=0):
        if front_key not in self.vertices.keys():
            _ = self.addVertex(front_key)
        elif tail_key not in self.vertices.keys():
            _ = self,addVertex(tail_key)
        return self.vertices[front_key].addNeighbor(self.vertices[tail_key],weight)

    def getVertices(self):
        return self.vertices.keys()
            

    
