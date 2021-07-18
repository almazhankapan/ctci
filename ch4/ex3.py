class Queue: 
    class NodeQueue: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self, value):
        newN=self.NodeQueue(value, None)
        if self.tail==None and self.head==None: 
            self.tail=newN
            self.head=newN
        else: 
            self.tail.next=newN
            self.tail=newN
    
    def dequeue(self):
        if self.head==None: 
            return None
        v=self.head.value
        self.head=self.head.next
        if self.head==None: 
            self.tail=None
        return v
    
    def isEmpty(self):
        return self.head==None

class LinkedList: 
    class NodeList: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
        self.size=0
    
    def insert(self, value):
        newN=self.NodeList(value, None)
        h=self.head
        if h==None: 
            self.head=newN
        else: 
            while(h.next!=None):
                h=h.next
            h.next=newN
        self.size+=1
    
    def delete(self, value):
        h=self.head
        if h.value==value: 
            self.head=self.head.next
        else: 
            while(h.next.value!=value):
                h=h.next
            h.next=h.next.next
        self.size-=1

    def print(self):
        h=self.head
        while h!=None: 
            print(str(h.value)+"->",end="")
            h=h.next
        print()

class BinaryTree: 
    class Node:
        def __init__(self, value, left=None, right=None) :
            self.value=value
            self.left=left
            self.right=right
            self.visited=False

        #important! for binary tree, for adding use breadth first search
        def add(self, root, node):
            if root==None: 
                return root
            q=Queue()
            q.enqueue(root)
            while(not q.isEmpty()):
                r=q.dequeue()
                if r.left==None: 
                    r.left=node
                    return
                elif r.right==None: 
                    r.right=node
                    return
                else: 
                    q.enqueue(r.left)
                    q.enqueue(r.right)

        def inorder_print(self, root):
            if root!=None: 
                self.inorder_print(root.left)
                #note that visiting is only for the core node
                # there are two recursive calls to left and right subtrees
                print(str(root.value))
                self.inorder_print(root.right)
    

    def __init__(self):
        self.root=None
    

    def listOfDepths(self, root, lists, level):
        #inorder
        if root==None: 
            return
        #level not in the list, first level is 0, and lists is empty-so create
        #a new linkedlist
        if len(lists)==level: 
            list=LinkedList()
            #levels traversed through 0 to i,so we already visited 
            #i-1 levels if we are at levelvi
            lists.append(list)
        else: 
            #otherwise we are on the same level
            list=lists[level]
        list.insert(root)
        #add nodes at the childrens' level
        #when we reach left leaf, its level=
        self.listOfDepths(root.left, lists, level+1)
        self.listOfDepths(root.right, lists, level+1)
    '''
    #breadth first search imp
    def listofDepths1(self,root) :
        lists=[]
        current=LinkedList()
        if root!=None: 
            current.insert(root)
        #here we have a linkedlist instead of a queue
        while(current.size!=0):
            #that's the visiting part
            lists.append(current)#add previous level
            parents=current
            current=LinkedList()
            h=current.head
            while(h!=None):
                if h.left!=None: 
                    current.insert(h.left)
                if h.right!=None: 
                    current.insert(h.right)
                h=h.next
        return lists
    '''
def main():
    t=BinaryTree()
    node1=t.Node(1)
    t.root=node1
    node2=t.Node(2)
    node3=t.Node(3)
    node4=t.Node(4)
    node5=t.Node(5)
    nodeLonely=t.Node(66)
    node1.add(t.root, node2)
    node1.add(t.root, node3)
    node1.add(t.root, node4)
    node1.add(t.root, node5)
    node1.add(t.root, nodeLonely)
    #t.root.inorder_print(t.root)
    #print(t.root.value)
    lists=[]
    t.listOfDepths(t.root, lists, 0)



if __name__=="__main__":
    main()            
        


            
                 
            

