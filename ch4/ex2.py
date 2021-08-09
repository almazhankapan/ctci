class BST: 
    class TreeNode: 
        def __init__(self, value):
            self.value=value
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
    def insert(self, value):
        if self.root==None: 
            self.root=self.TreeNode(value)
        else: 
            self.insertHelper(self.root, value)
    def insertHelper(self, node, value):
        if value<node.value:
            if node.left==None: 
                node.left=self.TreeNode(value)
                return
            else: 
                self.insertHelper(node.left, value) 
        else: 
            if node.right==None: 
                node.right=self.TreeNode(value)
                return
            else: 
                self.insertHelper(node.right, value) 

    def print(self):
        print(self.inorder_print(self.root, ""))
    
    def inorder_print(self, node, out):
        if node!=None: 
            out=self.inorder_print(node.left, out)
            out+=str(node.value)+"-"
            out=self.inorder_print(node.right, out)
        return out
    
    def buildMinTreeWrap(self, array):
        self.root=self.buildMinTree(array)

    
    def buildMinTree(self, array):
        mid=int(len(array)/2)
        root=self.TreeNode(array[mid])
        #important--return root if mid is 0 since
        #its an empty node by that time
        if mid==0:
            return root
        
        root.left=self.buildMinTree(array[0:mid])
        #very important--from mid+1 to end
        root.right=self.buildMinTree(array[(mid+1):len(array)])
        #return root after both left and right branches are done
        return root
    

def main():
    t=BST()
    t.buildMinTreeWrap([1,2,3,4,5,6,7])
    t.print()



if __name__=="__main__":
    main()