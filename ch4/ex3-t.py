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

class LinkedList: 
    class NodeList: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
    
    def insert(self, value):
        newN=self.NodeList(value, None)
        h=self.head
        if h==None: 
            self.head=newN
        else: 
            while(h.next!=None):
                h=h.next
            h.next=newN
    
    def delete(self, value):
        h=self.head
        if h.value==value: 
            self.head=self.head.next
        else: 
            while(h.next.value!=value):
                h=h.next
            h.next=h.next.next

    def print(self):
        h=self.head
        while h!=None: 
            print(str(h.value)+"->",end="")
            h=h.next
        print()

class Node: 
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        self.visited=False
    #insert in binary tree should be breadth first search
    def add(self, root, node):
        q=Queue()
        q.enqueue(root)
        while(not q.isEmpty()):
            r=q.dequeue()
            if r.left==None: 
                r.left=node
                return
            elif r.right==None: 
                r.right=node
                return
            else: 
                q.enqueue(r.left)
                q.enqueue(r.right)

def listOfDepths(root):
    '''
            5
        2        5
    4     7   8     11
    
    '''
    arr=[]
    ll=LinkedList()
    ll.append(root)
    arr.append(ll)
    q=Queue()
    q.enqueue(root)
    root.visited=True
    queue=[1,2,3,4,5,6]
    while(not q.isEmpty()):
        r=q.dequeue()
        r.visited=True
        ll=LinkedList()
        if r.left!=None and r.left.visited==False: 
            ll.append(r.left)
        if r.right!=None and r.right.visited==False: 
            ll.append(r.right)
        

        

         
