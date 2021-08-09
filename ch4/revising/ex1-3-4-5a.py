class LinkedList: 
    class ListNode: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
    def add(self, value):
        newN=self.ListNode(value, None)
        if self.head==None: 
            self.head=newN
            return
        h=self.head
        while(h.next!=None):
            h=h.next
        h.next=newN
    


class Queue: 
    class QueueNode: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, value):
        newN=self.QueueNode(value, None)
        if self.root==None: 
            self.root=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    def isEmpty(self):
        return self.head==None
    def dequeue(self):
        if self.head==None: 
            self.tail=None
            return None
        val=self.head.value
        self.head=self.head.next
        if self.head==None: 
            self.tail=None
        return val
class BinaryTree: 
    class TreeNode: 
        def __init__(self, value):
            self.value=value
            self.marked=False
            self.left=None
            self.right=None
    def __init___(self):
        self.root=None
    def cleanMarked(self, root):
        if root!=None: 
            if root.marked!=False: 
                root.marked=False
            self.cleanMarked(root.left)
            self.cleanMarked(root.right)
        return
    def insert(self, value):
        newN=self.TreeNode(value)
        self.cleanMarked(self.root)
        q=Queue()
        q.enqueue(self.root)
        self.root.marked=True
        while(not q.isEmpty()):
            node=self.dequeue()
            if node.left==None: 
                node.left=newN
                return
            elif node.right==None: 
                node.right=newN
            else: 
                if node.left.marked==False: 
                    node.left.marked=True
                    q.enqueue(node.left)
                if node.right.marked==False: 
                    node.right.marked=True
                    q.enqueue(node.right)
    #example 1
    def isRoute(self, node1,node2):
        self.cleanMarked(self.root)
        q=Queue()
        q.enqueue(node1)
        node1.marked=True
        while(not q.isEmpty()):
            node=self.dequeue()
            if node==node2:
                return True
            else: 
                if node.left.marked==False: 
                    node.left.marked=True
                    q.enqueue(node.left)
                if node.right.marked==False: 
                    node.right.marked=True
                    q.enqueue(node.right)

        return False
    #ex3
    def listOfDepths(self):
        arrays=[]
        if self.root==None: 
            return
        q=Queue()
        q.enqueue(self.root)
        count=1
        newCount=0
        while(not q.isEmpty()):
            ll=LinkedList() 
            while(count!=0):
                node=q.dequeue() 
                ll.add(node) 
                count-=1 
                if node.left!=None: 
                    if node.left.marked==False: 
                        node.left.marked=True
                        newCount+=1
                        q.enqueue(node.left)
                if node.right!=None: 
                    if node.right.marked==False: 
                        node.right.marked=True
                        newCount+=1
                        q.enqueue(node.right)
            arrays.append(ll) 
            count=newCount 
            newCount=0
        return arrays
    #ex4
    def getHeight(self, root):
        if root==None: 
            return -1 #leaf=-1
        else: 
            return (max(self.getHeight(root.left),self.getHeight(root.right))+1)
    #ex4
    def checkBalanced(self, root):
        return (1>=abs(self.getHeight(root.left)-self.getHeight(root.right)))        
    #ex5
    
    def validateBST(self):
        q=Queue()
        if self.root==None: 
            return True
        if self.root.left==None and self.root.right==None: 
            return True
        q.enqueue(self.root)
        self.root.marked=True
        while(not q.isEmpty()):
            node=q.dequeue()
            if node.left!=None: 
                if not(node.value>=node.left.value):
                    return False
                else: 
                    if node.left.marked==False: 
                        q.enqueue(node.left)
                        node.left.marked=True
            if node.right!=None: 
                if not(node.value<node.left.value):
                    return False
                else: 
                    if node.right.marked==False: 
                        q.enqueue(node.right)
                        node.right.marked=True
                


            

        
          

                
                


