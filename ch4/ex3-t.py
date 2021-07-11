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

class LinkedList: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
    
    def insert(self, value):
        newN=self.Node(value, None)
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
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.visited=False
    
    def add_child(self, Node):
        if self.left!=None: 
            self.right=Node
        else: 
            self.left=Node


def listOfDepths(root):
    lists=[]
    if root==None: 
        return
    ll=LinkedList()
    ll.insert(root.value)
    lists.append(ll)
    q=Queue()
    q.enqueue(root)
    root.visited=True
    while(not q.isEmpty()):
        r=q.dequeue()
        ll1=LinkedList()
        ll1.insert(r)
        lists.append(ll1)
        if r.left.visited==False: 
            q.enqueue(r.left)
            ll2=LinkedList()
            ll2.insert(r.left)
        if r.right.visited==False: 
            ll2.insert(r.right)
            q.enqueue(r.right)
