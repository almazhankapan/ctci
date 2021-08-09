class Queue: 
    class NodeQueue: 
        def __init__(self, value, next1):
            self.value=value
            self.next1=next1
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, value):
        new=self.NodeQueue(value, None)
        if self.tail==None: 
            self.head=new
            self.tail=new
        else: 
            self.tail.next1=new
            self.tail=new
    def dequeue(self):
        if self.head==None: 
            self.tail=None
            return None
        else: 
            val=self.head.value
            self.head=self.head.next1
            if self.head==None: 
                self.tail=None
            return val
    def isEmpty(self):
        return self.head==None
            
            

class Graph: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.children=[]
            self.marked=False
        def add(self, node):
            self.children.append(node)
    def __init__(self):
        self.root=None
        self.nodes=[]
    def add(self, node):
        self.nodes.append(node)

    def isRoute(self, node1,node2):
        #path-bfs
        q=Queue()
        q.enqueue(node1)
        node1.marked=True
        while(not q.isEmpty()):
            node=q.dequeue()
            node.marked=True
            #visit
            if node==node2:
                return True
            else: 
                for ch in node.children: 
                    if ch.marked==False: 
                        q.enqueue(ch)
                        ch.marked=True
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