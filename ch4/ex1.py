class Queue: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self, value):
        newN=self.Node(value, None)
        if self.tail==None and self.head==None: 
            self.tail=newN
            self.head=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    
    def dequeue(self):
        if self.head==None: 
            return None
        v=self.head.value
        self.head=self.head.next
        return v
    
    def isEmpty(self):
        return self.head==None


class Graph: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.children=[]
            self.visited=False
        
        def add_child(self, Node):
            self.children.append(Node)
        
        def remove_child(self, Node):
            for i in range(len(self.children)): 
                if self.children[i]==Node: 
                    del self.children[i]
    
    def __init__(self):
        self.nodes=[]

    def add(self, Node):
        self.nodes.append(Node)


def findRoute(node1,node2):
    #breadth first search
    q=Queue()
    node1.visited=True
    q.enqueue(node1)
    while(not q.isEmpty()):
        r=q.dequeue()
        for x in r.children():
            if x==node2:
                return True
            if not x.visited: 
                q.enqueue(x)
    return False
