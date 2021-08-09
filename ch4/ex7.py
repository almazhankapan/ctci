class Graph: 
    class GraphNode: 
        def __init__(self, value) -> None:
            self.value=value
            self.dependencies=0
            self.children=[]

    def __init__(self):
        self.nodes=[]
        self.edges=[]
    def findNode(self, value):
        for x in self.nodes: 
            if x.value==value: 
                return x
        return -1

def checkDependencies(projects):
    for x in projects: 
        if x.dependencies==0:
            return x
    return -1
    
def buildOrder2(projects, dependencies):
    #1. buildGraph
    g=Graph()
    
    for x in projects: 
        g.nodes.append(g.GraphNode(x))
    
    for pair in dependencies: 
        par=g.findNode(pair[0])
        child=g.findNode(pair[1])
        par.children.append(child)
        child.dependencies+=1
    
    #2. buildOrder
    order=[]
    current=None
    countNow=0
    countTotal=len(projects)
    found=False
    while(countNow!=countTotal):
        #note-iterate through graph nodes
        #checking the updated graph should be a separate function
        #if node has no incoming edges
        x=checkDependencies(g.nodes)
        if x!=-1:
            #delete from graph.nodes
            i=(g.nodes.index(x))
            del g.nodes[i]
            #decrement dependencies
            for child in x.children: 
                child.dependencies-=1
            #add to order array
            order.append(x.value)
            #add count+=1
            countNow+=1
        else: 
            return -1
    return order    
        





def buildOrder(projects, dependencies):
    g=Graph()
    order=[]
    count=0
   
    #create graph nodes
    for x in projects: 
        g.nodes.append(g.GraphNode(x))
    #add dependencies
    for pair in dependencies: 
        parent=g.findNode(pair[0])
        child=g.findNode(pair[1])
        child.dependencies+=1
        parent.children.append(child)
    i=0     

    while(count!=len(projects)):
        x=checkDependencies(g.nodes)
        if x==-1:
            return -1
        else: 
            count+=1
            i=(g.nodes).index(x)
            del g.nodes[i]
            order.append(x.value)
            for ch in x.children: 
                ch.dependencies-=1
                
                
                
    
    return order
        



def main():
    projects=['a','b','c','d','e','f']
    dependencies=[('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
    print(buildOrder(projects, dependencies))    
    print(buildOrder2(projects, dependencies))   
                
if __name__=="__main__":
    main()
              
                    
            

            
    
        
        

        


