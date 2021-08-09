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


class BST: 
    class TreeNode: 
        def __init__(self, value):
            self.value=value
            self.marked=False
            self.left=None
            self.right=None
            self.parent=None
    def __init__(self):
        self.root=None
    def cleanMarked(self, root):
        if root!=None: 
            if root.marked!=False: 
                root.marked=False
            self.cleanMarked(root.left)
            self.cleanMarked(root.right)
        return
    def insert(self, value):
        if self.root==None: 
            self.root=self.TreeNode(value)
        else: 
            self.insertHelper(self.root, value)

    
    def insertHelper(self, root, value):
        if root.value>value: 
            if root.left==None: 
                root.left=self.TreeNode(value)
                root.left.parent(root)
                return
            else: 
                self.insertHelper(root.left, value)
        elif root.value<=value: 
            if root.right==None: 
                root.right=self.TreeNode(value)
                root.right.parent(root)
                return
            else: 
                self.insertHelper(root.right, value)
    #ex2
    def minimalTree(self, array):
        mid=int(len(array)/2)
        root=self.TreeNode(array[mid])
        #return root! !!!!!if mid==0
        if mid==0:
            return root
        root.left=self.minimalTree(array[0:mid])
        root.right=self.minimalTree(array[mid+1])
        return root

    def leftmost(self, node):
        if node!=None: 
            while(node.left!=None):
                node=node.left
            return node
    
    def findSuccessor(self, node):
        #if has a right subtree, return leftmost
        if node.right!=None: 
            return self.leftmost(node.right)
        #if not, get the parent of parent-while
        # while it's not a left child
        else: 
            while(node==node.parent.right):
                node=node.parent
            return node.parent
        
                


    
    
    
    

    
        
        
            