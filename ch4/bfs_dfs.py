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

class Node: 
    def __init__(self, value):
        self.value=value
        self.visited=False
        self.children=[]

def visit(node):
    print(str(node.value)+"-", end="")

def dfs(node):
    if node==None: 
        return None
    visit(node)
    node.visited=True
    for x in node.children: 
        if x.visited==False: 
            bfs(x)
        
def bfs(node):
    q=Queue()
    q.enqueue(node)
    node.visited=True
    while(not q.isEmpty()):
        #dequeue a node from queue
        r=q.dequeue()
        #visit it and enqueue all of its children
        visit(r)
        for x in r.children: 
            if x.visited!=False: 
                q.enqueue(x)



