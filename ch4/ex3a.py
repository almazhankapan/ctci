class Queue: 
    class NodeQueue: 
        def __init__(self, value, next):
            self.value=value
            self.visited=False
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def enqueue(self, value):
        newN=self.NodeQueue(value, None)
        self.size+=1
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
            self.size-=1
            return v
    def isEmpty(self):
        return self.head==None


class LinkedList: 
    class NodeList: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
        self.size=0
    def add(self, value):
        newN=self.NodeList(value, None)
        if self.head==None: 
            self.head=newN
        else: 
            h=self.head
            while(h.next!=None):
                h=h.next
            h.next=newN
        self.size+=1
    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value.value)+"-",end="")
            h=h.next
        print()


class BinaryTree: 
    class Node: 
        def __init__(self,value ):
            self.value=value
            self.left=None
            self.right=None
            self.visited=False
    def __init__(self):
        self.root=None
    
    def add(self,node):
        self.cleanVisited(self.root)
        if self.root==None: 
            self.root=node
            return
        q=Queue()
        q.enqueue(self.root)
        self.root.visited=True
        while(not q.isEmpty()):
            r=q.dequeue()
            if r.left==None: 
                r.left=node
                return
            elif r.right==None: 
                r.right=node
                return
            else: 
                if r.left.visited==False: 
                    q.enqueue(r.left)
                    r.left.visited=True
                if r.right.visited==False: 
                    q.enqueue(r.right)
                    r.right.visited=True
    
    def listOfDepths(self):
        listOut=self.listOfDepthHelper(self.root)
        return listOut
    
    def print(self):
        out=self.inorder_print(self.root, "")
        print(out[0:(len(out)-1)])
    
    def inorder_print(self, root, traversal):
        if root!=None: 
            traversal=self.inorder_print(root.left,traversal)
            traversal+=str(root.value)+"-"
            traversal=self.inorder_print(root.right,traversal)
        return traversal
    def cleanVisited(self, r):
        if r==None: 
            return
        else: 
            if r.visited==True: 
                r.visited=False
            if r.left!=None: 
                self.cleanVisited(r.left)
            if r.right!=None: 
                self.cleanVisited(r.right)
    
        
        
    def listOfDepthHelper(self, root):
        self.cleanVisited(self.root)
        list=[]
        q=Queue()
        q.enqueue(root)
        root.visited=True
        while(not q.isEmpty()):
            size=q.size 
            while(size!=0):
                r=q.dequeue() 
                ll=LinkedList() 
                ll.add(r) #left
                if r.left!=None: 
                    if r.left.visited==False: 
                        r.left.visited=True 
                        q.enqueue(r.left) 
                if r.right!=None: 
                    if r.right.visited==False: 
                        r.right.visited=True
                        q.enqueue(r.right)
                size-=1
            list.append(ll)
        return list

def main():
    t=BinaryTree()
    node1=t.Node(1)
    node2=t.Node(2)
    node3=t.Node(3)
    node4=t.Node(4)
    node5=t.Node(5)
    nodeLonely=t.Node(66)
    t.add(node1)
    t.add(node2)
    t.add(node3)
    t.add(node4)
    t.add(node5)
    t.add(nodeLonely)
    t.print()
   
    lists=[]
    lists=t.listOfDepths()
    for i in lists: 
        i.print()
        print()

if __name__=="__main__":
    main()



