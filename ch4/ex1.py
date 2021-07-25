class Queue:
    class NodeQueue: 
        def __init__(self,value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, value):
        newN=self.NodeQueue(value,None )
        if self.tail==None: 
            self.tail=newN
            self.head=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    def dequeue(self):
        if self.head==None: 
            self.tail=None
            return None
        else: 
            v=self.head.value
            self.head=self.head.next
            if self.head==None: 
                self.tail=None
            return v
    def isEmpty(self):
        return self.head==None

class Graph: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.children=[]
            self.visited=False
        def add(self, child):
            self.children.append(child)
    def __init__(self):
        self.nodes=[]
    def add(self, node):
        self.nodes.append(node)
    
    def isRoute(self, node1,node2):
        #breadth first search
        q=Queue()
        q.enqueue(node1)
        node1.visited=True
        while(not q.isEmpty()):
            r=q.dequeue()
            if r.value==node2.value:
                return True
            else: 
                for child in r.children: 
                    if child.visited==False: 
                        q.enqueue(child)
                        child.visited=True
        return False

def main():
    g=Graph()
    node1=g.Node(1)
    node2=g.Node(2)
    node3=g.Node(3)
    node4=g.Node(4)
    node5=g.Node(5)
    node6=g.Node(6)
    node3.children=[node2,node4,node5]
    node1.add(node3)
    print(g.isRoute(node1,node3))
    print(g.isRoute(node1,node6))

if __name__=="__main__":
    main()


        
        

            