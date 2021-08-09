class Queue: 
    class QueueNode: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def enqueue(self, value):
        newN=self.QueueNode(value, None)
        if self.tail==None: 
            self.head=newN
            self.tail=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    def dequeue(self):
        if self.head==None: 
            self.tail=None
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
        def __init__(self, value) -> None:
            self.value=value
            self.marked=False
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
    def print(self):
        print(self.inorder_print(self.root, ""))
    
    def inorder_print(self, root, out):
        if root!=None: 
            out=self.inorder_print(root.left, out)
            out+=str(root.value)+"-"
            out=self.inorder_print(root.right, out)
        return out

    def clearMarked(self, root):
        if root==None: 
            return
        if root.marked==True: 
            root.marked=False
        self.clearMarked(root.left)
        self.clearMarked(root.right)

    def insert(self, value):
        self.clearMarked(self.root)
        newN=self.TreeNode(value)
        if self.root==None: 
            self.root=newN
        else: 
            q=Queue()
            q.enqueue(self.root)
            self.root.marked=True
            while(not q.isEmpty()):
                node=q.dequeue()
                #visit node
                if node.left==None: 
                    node.left=newN
                    return
                if node.right==None: 
                    node.right=newN
                    return
                else: 
                    if node.left.marked==False: 
                        node.left.marked=True
                        q.enqueue(node.left)
                    if node.right.marked==False: 
                        node.right.marked=True
                        q.enqueue(node.right)

    def validate(self):
        #bfs - check if bintree is bst
        #base cases
        if self.root==None: 
            return True
        elif self.root.left==None and self.root.right==None: 
            return True
        else: 
            self.clearMarked(self.root)
            q=Queue()
            q.enqueue(self.root)
            self.root.marked=True
            while(not q.isEmpty()):
                node=q.dequeue()
                if node.left!=None: 
                    if not(node.value>=node.left.value):
                        return False
                if node.right!=None: 
                    if not(node.value<node.right.value):
                        return False
                else: 
                    if node.left!=None: 
                        if node.left.marked==False: 
                            q.enqueue(node.left)
                            node.left.marked=True
                    if node.right!=None:
                        if node.right.marked==False: 
                            q.enqueue(node.right)
                            node.right.marked=True
            #dont forget to return True in the end
            return True
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
    print(t.validate())
    #      1
    #   2      3
    # 4   5  66
    t2=BinaryTree()
    node2=t2.TreeNode(10)
    t2.root=node2
    t2.insert(5)
    t2.insert(13)
    t2.insert(4)
    t2.insert(7)
    t2.insert(11)
    t2.print()
    print(t2.validate())
    #      10
    #   5      13
    # 4   7  11

if __name__=="__main__":
    main()

                         
                    
                    


            
