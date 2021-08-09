class Graph: 
    class GraphNode: 
        def __init__(self, value):
            self.value=value
            self.children=[]
            self.dependencies=0
        def addChild(self, node):
            self.children.append(node)
    def __init__(self):
        self.nodes=[]
        self.edges=[]
    def add(self, node):
        self.nodes.append(node)
    def addEdges(self, node1,node2):
        edge=(node1,node2)
        node1.children.append(node2)
        self.edges.append(edge)
    def findNode(self, value):
        for x in self.nodes: 
            if x.value==value: 
                return x


def checkDependency(array):
    #find nodes with zero dependencies
    for x in array: 
        if x.dependencies==0:
            return x
    return -1

def buildOrder(self, projects, dependencies):
    #build graph
    g=Graph()
    for x in projects: 
        g.add(g.GraphNode(x))
    #build dependencies
    for d in dependencies:
        #important!! you have to find node for each dependency or create one
        # but if you create- you might miss independent nodes 
        node1=g.findNode(d[0])
        node2=g.findNode(d[1])
        node1.addChild(node2)
        node2.dependencies+=1
    
    #build order
    order=[]
    #while all projects are not processed
    count=0
    totalCount=len(projects)
    while(count!=totalCount):
        #for each node in projects, check if it has dependencies
        node=checkDependency(g.nodes)
        if node==-1:
            return False
        else: 
            #add node to order array
            order.append(node.value)
            count+=1
            #once find a node with no dependencies, remove it
            #from graph and decrement dependencies of the children
            i=g.nodes.index(node)#find index of the element
            del g.nodes[i]#delete it from graph
            #decrement node children's dependencies
            for child in node.children: 
                child.dependencies-=1
    return order        
        

    
    
