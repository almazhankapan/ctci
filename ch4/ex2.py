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
        out=self.inorder_print(self.root, "")
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

    def inorder_print(self, root, traversal):
        if root!=None: 
            traversal=self.inorder_print(root.left, traversal)
            traversal+=str(root.value)+"-"
            traversal=self.inorder_print(root.right, traversal)
        return traversal

    def buildMinTree(self, array):
        self.root=self.minTreeHelper(array)
        #            5
        #        4       7
        #    1     3   6    9

    def minTreeHelper(self, array): 
        mid=int(len(array)/2)#3 #1 #0
        #important!!make sure to create the node! 
        root=self.Node(array[mid])#5 #4 # #1
        if mid==0:
            return root #return the element if mid=0
        root.left=self.minTreeHelper(array[0:mid]) #1
        root.right=self.minTreeHelper(array[(mid+1): (len(array))])
        return root
    

def main():
    t=BST()
    t.buildMinTree([1,2,3,4,5,6,7])
    t.print()



if __name__=="__main__":
    main()
    