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
        if key not in self.vertices.keys():
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
        return [x for x in self.vertices.keys()]
            

    

g = Graph()
for i in range(6):
    print(g.addVertex(i))
print(g.getVertices())
print(g.addEdge(0,1,5))
print(g.addEdge(0,5,2))
print(g.addEdge(1,2,4))
print(g.addEdge(2,3,9))
print(g.addEdge(3,4,7))
print(g.addEdge(3,5,3))
print(g.addEdge(4,0,1))
print(g.addEdge(5,4,8))
print(g.addEdge(5,2,1))
for _ ,v in g.vertices.items():
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
