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
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=(str(root.value)+"-")
            out=self.inorder_print(root.right, out)
        return out
    def print(self):
        print(self.inorder_print(self.root, ""))

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
    def descendant(self, node1,node2,out):
        if node1!=None: 
            if node1.left==node2 or node1.right==node2:
                out=True
            else: 
                out=self.descendant(node1.left, node2,out) 
                if out!=True: 
                    out=self.descendant(node1.right, node2,out)
        return out

    def findCommonAnc(self, node1,node2):
        if self.descendant(self.root, node1,None) and self.descendant(self.root, node2,None) :
            return self.findCommonAncHelp(self.root, node1,node2)
        elif self.descendant(self.root, node1,None) and not self.descendant(self.root, node2,None):
            return node1
        elif self.descendant(self.root, node2,None) and not self.descendant(self.root, node1,None):
            return node2
        else: 
            return None

    def findCommonAncHelp(self, root, node1,node2):
        #THE MOST IMPORTANT THING---MAKE SURE TO PUT ROOT!=NONE in FINDCOMMONANCHELPER
        # and later return root
        if root!=None: 
            #if both are descendants of the the left node, search in the left subtree, same for right
            if self.descendant(root.left, node1,None) and self.descendant(root.left, node2,None):
                root=self.findCommonAncHelp( root.left, node1,node2)
            elif self.descendant(root.right, node1,None) and self.descendant(root.right, node2,None):
                root=self.findCommonAncHelp( root.right, node1,node2)
            else: #otherwise return current root
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
    a=t2.findCommonAnc(node10,node16)
    if a!=None: 
        print(a.value)
    else: 
        print("None")
    
if __name__=="__main__":
    main()
                                              
        

            
