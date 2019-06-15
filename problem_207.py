class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.children = []
        self.color = None

    def addChild(self,c):
        self.children.append(c)



class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self,key,val):
        n = Node(key,val)
        self.vertices[key] = val
        
    def addEdge(self,key1,key2):
        self.addChild(key1,key2)
        self.addChild(key2,key1)


    def addChild(self,parent,child):
        if parent not in self.vertices:
            p = Node(parent,parent)
            self.vertices[parent] = p
        
        if child not in self.vertices:
            c = Node(child,child)
            self.vertices[child] = c

        self.vertices[parent].addChild(self.vertices[child])

    def printGraph(self):
        for d in self.vertices.keys():
            print(self.vertices[d].val,'color',self.vertices[d].color)
            for c in self.vertices[d].children:
                print(c.val)
            print('###')

def isBipartite(g,s):
    if s not in g.vertices:
        raise Exception("start vertex does not exist")

    queue = [g.vertices[s]]
    g.vertices[s].color = 1
    visited = set()
    while len(queue) > 0:
        nq = []
        for v in queue:
            color = 1 if v.color==2 else 2
            
            for c in v.children:
                if c.color!=None and c.color != color:
                    return False
                if c.key not in visited:
                    c.color = color
                    nq.append(c)
                    visited.add(c.key)

        queue = nq
    return True


g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)

print(isBipartite(g,1))

g2 = Graph()
g2.addEdge(1,2)
g2.addEdge(1,3)
g2.addEdge(3,4)
g2.addEdge(2,4)
print(isBipartite(g2,1))

g3 = Graph()
g3.addEdge(1,2)
g3.addEdge(1,3)
g3.addEdge(4,2)
g3.addEdge(5,2)
g3.addEdge(3,4)
g3.addEdge(3,5)
print(isBipartite(g3,1))
