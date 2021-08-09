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

    def insert(self, value):
        newN=self.TreeNode(value)
        if self.root==None: 
            self.root=newN
            self.root.parent=None
        else: 
            self.insertHelper(self.root, value)
    
    def print(self):
        print(self.inorder_print(self.root, ""))
    
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=str(root.value)+"-"
            out=self.inorder_print(root.right, out)
        return out

    def insertHelper(self, root, value):
        if root!=None: 
            if value<=root.value: 
                if root.left==None: 
                    root.left=self.TreeNode(value)
                    root.left.parent=root
                    return
                else: 
                    self.insertHelper(root.left, value)
            else: 
                if root.right==None: 
                    root.right=self.TreeNode(value)
                    root.right.parent=root
                    return
                else: 
                    self.insertHelper(root.right, value)
        return
    #             10
    #      6             13
    #   4     8      11        15
    # 3   5  7  9  10.5 12   14   16


    def findSuccessor(self, node):
        #1. if node has right child, its successor is the
        #leftmost node of the right child
        if node.right!=None: 
            return self.leftmost(node.right)
        #otherwise, go up and find the parent which is a left child and
        #return grandparent--see example of 9
        else: 
            while(node==node.parent.right):
                node=node.parent
            return node.parent
    
    def leftmost(self, node):
        while(node.left!=None):
            node=node.left
        return node
        

        
        
        
        
        

        

    


def main():
    t2=BST()
    root=t2.TreeNode(10)
    node6=t2.TreeNode(6)
    node13=t2.TreeNode(13)
    node4=t2.TreeNode(4)
    node8=t2.TreeNode(8)
    node11=t2.TreeNode(11)
    node15=t2.TreeNode(15)
    node3=t2.TreeNode(3)
    node5=t2.TreeNode(5)
    node7=t2.TreeNode(7)
    node9=t2.TreeNode(9)
    node12=t2.TreeNode(12)
    node14=t2.TreeNode(14)
    node16=t2.TreeNode(16)
    node10=t2.TreeNode(10.5)
    root.left=node6
    root.right=node13
    node6.left=node4
    node6.right=node8
    node13.left=node11
    node13.right=node15
    node4.left=node3
    node4.right=node5
    node8.left=node7
    node8.right=node9
    node11.left=node10
    node11.right=node12
    node15.left=node14
    node15.right=node16
    node6.parent=root
    node13.parent=root
    node4.parent=node6
    node8.parent=node6
    node11.parent=node13
    node15.parent=node13
    node3.parent=node4
    node5.parent=node4
    node7.parent=node8
    node9.parent=node8
    node10.parent=node11
    node12.parent=node11
    node14.parent=node15
    node16.parent=node15
    root.parent=None
    t2.root=root

    t2.print()
    node=t2.findSuccessor(node9)
    if node==None: 
        print("No successor")
    else: 
        print(node.value)
    
    #check leftmost function
    print("leftmost-check: ")
    print(t2.leftmost(t2.root).value)

    '''
    #check if insert works
    t2.insert(10)
    t2.insert(6)
    t2.insert(13)
    t2.insert(4)
    t2.insert(8)
    t2.insert(11)
    t2.insert(15)
    t2.insert(3)
    t2.insert(5)
    t2.insert(7)
    t2.insert(9)
    t2.insert(10.5)
    t2.insert(12)
    t2.insert(14)
    t2.insert(16)
    t2.print()
    '''
    #             10
    #      6             13
    #   4     8      11      15
    # 3   5  7  9  10.5  12  14   16
    #successor of 9 is 
    # if node is a left child, successor is the parent
    # if node is a right child (9)
    #   --if its in left subtree, successor is parent's parent?  
    #   --if its in right subtree, successor is parent's parent's parent e
    #    
if __name__=="__main__":
    main()

         


    
