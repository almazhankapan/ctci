class Tree: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.children=[]
        #Note! !! adding function is inside Node, not Tree
        def add(self, value):
            self.children.append(value)
    
    def __init__ (self):
        self.root=self.Node(None) 
        self.children=[]
    #note--you need add functions to both tree and node
    def addNode(self, node):
        self.children.append(node)
        

class BinaryTree: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.left=None
            self.right=None
        
        #adding to node! not tree
        def add(self, value):
            n=self.Node(value)
            if self.left==None: 
                self.left=n
            elif self.left.value>value: 
                o=self.left
                self.left=n
                self.right

    def __init__(self):
        self.root=self.Node(None)
    
    def inorder(self, node):
        self.inorder(node.left)
        print(str(node.value)+"-",end="")
        self.inorder(node.right) 

    def preorder(self, node):
        print(str(node.value)+"-",end="")
        self.preorder(node.left)
        self.preorder(node.right)
    
    def postorder(self, node):
        self.postorder(node.left)
        self.postorder(node.right)
        print(str(node.value)+"-")
    
    

def main():
    tree=Tree()
    tree.root.add(5)
    
    
