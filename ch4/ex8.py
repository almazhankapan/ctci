class Queue: 
    class NodeQueue: 
        def __init__(self, value, next1):
            self.value=value
            self.next1=next1
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self, value):
        new=self.NodeQueue(value, None)
        if self.tail==None: 
            self.head=new
            self.tail=new
        else: 
            self.tail.next1=new
            self.tail=new
    def dequeue(self):
        if self.head==None: 
            self.tail=None
            return None
        else: 
            val=self.head.value
            self.head=self.head.next1
            if self.head==None: 
                self.tail=None
            return val
    def isEmpty(self):
        return self.head==None


class BinaryTree: 
    class TreeNode: 
        def __init__(self, value) -> None:
            self.value=value
            self.left=None
            self.right=None
            self.marked=False
    def __init__(self) -> None:
        self.root=None
    def cleanMarked(self, root):
        if root!=None: 
            if root.marked!=False: 
                root.marked=False
            self.cleanMarked(root.left)
            self.cleanMarked(root.right)
        else: 
            return
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=(str(root.value)+"-")
            out=self.inorder_print(root.right, out)
        return out
    def print(self):
        print(self.inorder_print(self.root, ""))
            
    def insert(self, value):
        self.cleanMarked(self.root)
        q=Queue()
        q.enqueue(self.root)
        self.root.marked=True
        while(not q.isEmpty()):
            node=q.dequeue()
            if node.left==None: 
                node.left=self.TreeNode(value)
                return
            if node.right==None: 
                node.right=self.TreeNode(value)
                return
            else: 
                if node.left.marked==False: 
                    node.left.marked=True
                    q.enqueue(node.left)
                if node.right.marked==False: 
                    node.right.marked=True
                    q.enqueue(node.right)
    def firstCommon(self, node1,node2):
        #if both nodes are in the tree
        if self.descendant(self.root, node1) and self.descendant(self.root, node2):
            return self.firstCommonAncestor(self.root,node1,node2 )
        #if node2 is not in the tree
        elif self.descendant(self.root, node1) and not self.descendant(self.root, node2):
            return node1
        #if node1 is not in the tree
        elif self.descendant(self.root, node2) and not self.descendant(self.root, node1):
            return node2
        else: 
            return None
    def descendant(self, root, node):
        if root!=None: 
            if root.left==node or root.right==node: 
                return True
            else: 
                if self.descendant(root.left, node):
                    return True
                #search for the right descendant 
                else: 
                    return self.descendant(root.right, node)
            
    #        10
#      6             13
#   4     8      11      15
# 3   5  7  9  10.5  12  14   16
    def firstCommonAncestor(self, root, node1,node2):
        if root!=None: 
            #if both are descendants of the left return left
            if self.descendant(root.left, node1) and self.descendant(root.left, node2):
                root=self.firstCommonAncestor(root.left, node1,node2)
            #if both are descendants of the right return right
            elif self.descendant(root.right, node1) and self.descendant(root.right, node2): 
                root=self.firstCommonAncestor(root.right, node1,node2)
            else: 
                return root
        return root
            
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
    a=t2.firstCommon(node10,node16)
    if a!=None: 
        print(a.value)
    else: 
        print("None")
    
if __name__=="__main__":
    main()
                                              
        
