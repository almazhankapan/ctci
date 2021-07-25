class BST: 
    class Node: 
        def __init__(self, value):
            self.value=value
            self.left=None
            self.right=None
            self.visited=False
    def __init__(self):
        self.root=None
    
    def add(self, node):
        if self.root==None: 
            self.root=node
            return
        else: 
            self.preorder_add(self, self.root, node)
    
    def print(self):
        out=self.preorder_print(self.root, "")
        print(out[0:(len(out)-1)])

    def preorder_add(self, root, node):
        if root.value<=node.value: 
            if root.left==None: 
                root.left=node
            else: 
                self.preorder_add(root.left, node)
        else: 
            if root.right==None: 
                root.right=node
            else: 
                self.preorder_add(root.right, node)

    def preorder_print(self, root, traversal):
        if root!=None: 
            traversal+=str(root.value)+"-"
            traversal=self.preorder_print(root.left, traversal)
            traversal=self.preorder_print(root.right, traversal)
        return traversal


