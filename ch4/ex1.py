
class Graph: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.children=[]
            self.visited=False

        def add(self, node):
            self.children.append(node)
    class Queue: 
        class NodeQueue: 
            def __init__(self, value, next):
                self.value=value
                self.next=next
        
        def __init__(self):
            self.head=None
            self.tail=None

        def enqueue(self, value):
            newN=self.NodeQueue(value, None)
            if self.tail==None: 
                self.tail=newN
                self.head=newN
            else: 
                self.tail.next=newN
                self.tail=newN
        
        def dequeue(self):
            if self.head==None: 
                return None
            else: 
                v=self.head.value
                self.head=self.head.next
                if self.head==None: 
                    self.tail=None
                return v
        
        def isEmpty(self):
            return self.head==None

    def __init__(self):
        self.nodes=[]
    
    def add(self, node):
        self.nodes.append(node)
    
    def findRoutes(self, node1,node2):
        q=self.Queue()
        #node1,node2--children 
        q.enqueue(node1)
        node1.visited=True
        while (not q.isEmpty()):
            r=q.dequeue()#get value-which is Node
            if r==node2:
                return True
            for x in r.children: 
                if x.visited==False: 
                    q.enqueue(x)
                    x.visited=True
        return False


def main():
    g=Graph()
    node1=g.Node(12)
    node2=g.Node(13)
    node3=g.Node(17)
    node4=g.Node(5)
    node5=g.Node(9)
    nodeLonely=g.Node(88)
    node1.add(node2)
    node1.add(node3)
    node3.add(node4)
    node4.add(node5)
    g.nodes=[node1,node2,node3,node4,node5,nodeLonely]
    print(g.findRoutes(node1,node2))
    print(g.findRoutes(node1,nodeLonely))


if __name__=="__main__":
    main()

       

    
