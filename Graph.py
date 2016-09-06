# Directed/Undirected Graphs
# Adjacency List
# This implementation also works for weighted graphs.
# Includes Breadth First Search (BFS)

from collections import deque

class Vertex(object):

    def __init__ (self,key):
        self.id = key
        self.connections = {}
        self.distance = 0
        self.pred = None

    def addConnection(self,nbr,weight=0):
        self.connections[nbr] = weight
        return True

    def getConnections(self):
        return list(self.connections.keys())

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connections[nbr]

    def getDegree(self):
        return len(self.connections)

    def __structure__(self):
        return str(self.id)+ ' connected to: ' + str([x for x in self.connections.keys()])

    def setDistance(self,d):
        self.distance = d

    def setPred(self,p):
        self.pred = p

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.pred

class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.graph_size = 0

    def addVertex(self,key):
        if key not in self.vertices.keys():
            self.vertices[key] = Vertex(key)
            self.graph_size += 1
            return True
        else:
            print('Key exist')
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
        return self.vertices[front_key].addConnection(tail_key,weight)

    def getVertices(self):
        return list(self.vertices.keys())
            
    def __structure__(self):
        for v in self.vertices.values():
            for key in v.getConnections():
                print ('(%s ,%s)' % (v.getId(),key))

    def getDistance(self,start,end):
        self.bfs(start)
        return self.getVertex(end).distance

    def bfs(self,start_key):
        q = deque()
        colors = {x:0 for x in self.getVertices()}
        v = self.vertices[start_key]
        v.setPred(start_key)
        q.append(v)
        while len(q) > 0:
            vfront = q.pop()
            for key in vfront.getConnections():
                if colors[key] == 0:
                    v = g.getVertex(key)
                    q.append(v)
                    colors[key] = 1
                    v.setPred(vfront.getId())
                    v.setDistance(vfront.getDistance()+1)
            colors[vfront.getId()] =2
        #for v in self.vertices.values():
        #    print('distance between vertex %s and %s is %i edge(s)'% (start_key,v.getId(),v.distance))

                
    

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
g.__structure__()
#g.bfs(2)
print(g.getDistance(2,1))
