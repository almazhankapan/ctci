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


def checkTrees(root1,root2,out):
    if root1!=None and root2!=None: 
        out=(root1.value==root2.value)
        left=checkTrees(root1.left, root2.left, out)
        if left: 
            out=checkTrees(root1.right, root2.right, out)
        else: 
            out=False
    if root1!=None and root2==None: 
        return False
    if root2!=None and root1==None: 
        return False
    else: 
        return out
   

    
    

def checkSubtree(t1,t2):
    t1.cleanMarked(t1.root)
    t2.cleanMarked(t2.root)
    q=Queue()
    q.enqueue(t1.root)
    t1.root.marked=True
    while(not q.isEmpty()):
        node=q.dequeue()
        if node==t2.root: 
            out=checkTrees(node, t2.root, None)
            if out: 
                return True
        else: 
            if node.left!=None: 
                if node.left.marked==False: 
                    node.left.marked=True
                    q.enqueue(node.left)
            if node.right!=None: 
                if node.right.marked==False: 
                    node.right.marked=True
                    q.enqueue(node.right)
    return False
            
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
    t3=BinaryTree()
    t3.root=node8
    t2.print()
    print(checkSubtree(t2,t3))
    print(checkTrees(node11, node6, None))
#             10
#      6             13
#   4     8      11      15
# 3   5  7  9  10.5  12  14   16
if __name__=="__main__":
    main()
                                              
        
