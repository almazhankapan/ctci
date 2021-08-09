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
        def __init__(self, value):
            self.value=value
            self.left=None
            self.right=None
            self.marked=True
    def __init__(self):
        self.root=None
    

    def clearMarked(self, root):
    #dfs
        if root!=None: 
            if root.marked==True: 
                root.marked=False
            self.clearMarked(root.left)
            self.clearMarked(root.right)
        return
    def insert(self, value):
        self.clearMarked(self.root)
        if self.root==None: 
            self.root=self.TreeNode(value)
        else: 
            self.insertHelper(self.root, value)

    def insertHelper(self, node, value):
        q=Queue()
        q.enqueue(node)
        node.marked=True
        while(not q.isEmpty()):
            n=q.dequeue()
            if n.left==None: 
                n.left=self.TreeNode(value)
                return
            elif n.right==None: 
                n.right=self.TreeNode(value)
                return
            else: 
                if n.left.marked==False: 
                    q.enqueue(n.left)
                    n.left.marked=True
                if n.right.marked==False: 
                    q.enqueue(n.right)
                    n.right.marked=True

#      1
#   2      3
# 4   5  66
#looks like bfs

    def getHeight(self, root):
        if root!=None: 
            return max(self.getHeight(root.left),self.getHeight(root.right))+1
        else: 
            return -1
    # getHeight(root)--1+1=2
    #   getHeight(1)-->left--0+1=1
    #       getHeight(2)-->left--(-1+1=0)
    #           getHeight(4)---left-->-1---->
    #           getheight(4)--right-->-1--->
    #       getHeight(2)-->right--(1+1=0)
    #           getHeight(5)---left-->-1---->
    #           getheight(5)--right-->-1--->
    #   getHeight(1)-->right--=0+1=1
    #       getHeight(3)-->left--(-1+1)=0
    #            getHeight(66)-->left---1
    #       getHeight(3)-->right--(-1)  


    def checkBalanced(self, root):
        diff=abs(self.getHeight(root.left)-self.getHeight(root.right))
        return 1>=diff

    def print(self):
        print(self.inorder_print(self.root, ""))
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=(str(root.value)+"-")
            out=self.inorder_print(root.right, out)
        return out
def main():
    t=BinaryTree()
    node1=t.TreeNode(1)
    t.root=node1
    t.insert(2)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    t.insert(66)
    t.print()
    lists=[]
    print(t.getHeight(t.root))
    print(t.checkBalanced(t.root))
    #      1
    #   2      3
    # 4   5  66

if __name__=="__main__":
    main()


        
