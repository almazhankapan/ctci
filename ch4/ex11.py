class Queue: 
    class QueueNode: 
        def __init__(self, value, next) -> None:
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, value):
        newN=self.QueueNode(value, None)
        if self.tail==None: 
            self.tail=newN
            self.head=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    def dequeue(self):
        if self.head==None: 
            return None
        val=self.head.value
        self.head=self.head.next
        if self.head==None: 
            self.tail=None
        return val
    def isEmpty(self):
        return self.head==None
        


class BinaryTree: 
    class TreeNode: 
        def __init__(self, value):
            self.value=value
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
    #def insert(self, value)

    def find(self, value):
        return self.findHelper(self.root, value, None)
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=(str(root.value)+"-")
            out=self.inorder_print(root.right, out)
        return out
    def print(self):
        print(self.inorder_print(self.root, ""))
    def findHelper(self, root, node, out):
        if root!=None: 
            if root.value==node.value: 
                out=root
            else:  
                out=self.findHelper(root.left, node, out)
                if out==None:
                    out=self.findHelper(root.right, node, out)
        return out
    def findRightMost(self, non):
        root=self.root
        while(root.right!=None):
            root=root.right
        return root
        
    def delete(self, node):
        parent=self.findParent(node)
        rightNode=self.findRightMost()
        if node!=rightNode: 
            new=self.findRightMost()
        if parent==None: 
            if parent.left==node: 
                parent.left=rightNode
        
        
        
        
        
        else: 
            rightNode=self.findRightMost()
            if node==rightNode: 
                new=self.findRightMost()
                
    def findParent(self, fnode):
        self.cleanMarked(self.root)
        q=Queue()
        self.root.marked=True
        parent=None
        if fnode.value==self.root.value: 
            return parent
        q.enqueue(self.root)
        while(not q.isEmpty()):
            node=q.dequeue()
            if node.left!=None: 
                if fnode.value==node.left.value: 
                    parent=node
                    return node
            if node.right!=None: 
                if fnode.value==node.right.value: 
                    parent=node
                    return node
            if node.left.marked==False: 
                node.left.marked=True
                q.enqueue(node.left)
            if node.right.marked==False: 
                node.right.marked=True
                q.enqueue(node.right)


    '''
        3
     4    5
   1  4 5   6 
    
    '''


def main():
    t2=BinaryTree()
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
    t2.root=root

    t2.print()
    print(t2.find(node15).value)
    
if __name__=="__main__":
    main()
                                          
    