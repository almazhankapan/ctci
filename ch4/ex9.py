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
    def cleanMarked(self, root):
        if root!=None: 
            if root.marked!=False: 
                root.marked=False
            self.cleanMarked(root.left)
            self.cleanMarked(root.right)
        else: 
            return
    #             10
    #      6             13
    #   4     8      11      15

    # 10,6,13         10, 13, 6
    #  10 6/13    4/8/11/15
    # 1*2* 4=8 options
    def findArr(self):
        arrays=[]
        self.findArrays2([],self.root, arrays)
        print(arrays)

    def findArrays2(self, array, root, arrays):
        if root!=None: 
            array.append(root.value) #10
            if root.left!=None: 
                self.findArrays2(array, root.left, arrays) #10,6 --#10,6,4--#10,6,8
            if root.right!=None: 
                self.findArrays2(array, root.right, arrays)   #10,13--#10,13,11-_#10,13,15
        #this one always happens--
        arrays.append(array)

                        

def main():
    t2=BST()
    #check if insert works
    t2.insert(10)
    t2.insert(6)
    t2.insert(13)
    t2.insert(4)
    t2.insert(8)
    t2.insert(11)
    t2.insert(15)
    t2.print()
    t2.findArr()
    
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

         


    
