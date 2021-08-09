class LinkedList: 
    class ListNode: 
        def __init__(self, value, next) -> None:
            self.value=value
            self.next=next
    def __init__(self) -> None:
        self.head=None
    def add(self, value):
        new=self.ListNode(value, None)
        if self.head==None: 
            self.head=new
        else: 
            h=self.head
            while(h.next!=None):
                h=h.next
            h.next=new
    def print(self):
        h=self.head
        while(h!=None):
            print(str((h.value).value)+"-",end="")
            h=h.next
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
            self.marked=False
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
            return
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
            if node.left.marked==False: 
                q.enqueue(node.left)
                node.left.marked=True
            if node.right.marked==False: 
                q.enqueue(node.right)
                node.right.marked=True



    def print(self):
        print(self.inorder_print(self.root, ""))
    

    def listOfDepths(self):
        self.clearMarked()
        out=[]
        q=Queue()
        q.enqueue(self.root)
        #important! -mark root as True
        self.root.marked=True
        #don't forget to add count as 1
        count=1
        new_count=0
        while(not q.isEmpty()):
            ll=LinkedList()
            while(count!=0):
                count-=1
                node=q.dequeue()
                ll.add(node)
                if node.left!=None: 
                    if node.left.marked==False: 
                        node.left.marked=True
                        new_count+=1
                        q.enqueue(node.left)
                if node.right!=None:
                    if node.right.marked==False: 
                        node.right.marked=True
                        new_count+=1
                        q.enqueue(node.right)
            count=new_count
            new_count=0
            #append linked list inside the main loop
            out.append(ll)
                


    def inorder_print(self, node, out):
        if node!=None: 
            out=self.inorder_print(node.left, out)
            out+=(str(node.value)+"-")
            out=self.inorder_print(node.right, out)
        return out

            #          2
            #      3      6
            #   4   7   5    8
            # 11 3 4 5 6 7  8 9

    def listOfDepths(self, root):
        #make sure to clear all marked nodes
        #bfs
        self.clearMarked(self.root)
        array=[]
        q=Queue()
        q.enqueue(root)
        root.marked=True
        count=1
        new_count=0
        while(not q.isEmpty()):
            #create a linked list for each level
            ll=LinkedList()  
            #count nodes at one level
            while(count!=0):
                node=q.dequeue() 
                count-=1 
                ll.add(node) 
                if node.left!=None: 
                    if node.left.marked==False: 
                        q.enqueue(node.left)
                        #new level's count
                        new_count+=1 #new_count=1,3
                        node.left.marked=True
                if node.right!=None: 
                    if node.right.marked==False: 
                        q.enqueue(node.right)
                        new_count+=1 #new_count=2
                        node.right.marked=True
            count=new_count
            new_count=0
            array.append(ll)
        return array

    def printListOfDepths(self):
        array=self.listOfDepths(self.root)
        for list in array: 
            list.print()
            print()

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
    t.printListOfDepths()
    #      1
    #   2      3
    # 4   5  66

if __name__=="__main__":
    main()
