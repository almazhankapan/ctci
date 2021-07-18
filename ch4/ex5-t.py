#bst with minimum height
class BST: 
    class Node: 
        def __init__(self, value, left=None, right=None):
            self.value=value
            self.left=left
            self.right=right
            '''
            6
              10
            5      15
        3     7  13  19
        '''
        def add(self, root, node):
            if root!=None: 
                if node.value<=root.value: 
                    if root.left==None: 
                        root.left=node
                        return
                    self.add(root.left, node) 
                else: 
                    if root.right==None: 
                        root.right=node
                        return
                    self.add(root.right, node)

        def validate(self, root):
            q=self.Queue()
            root.visited=True
            q.enqueue(root)
            while(not q.isEmpty()):
                r=q.dequeue()
                if r.left.value<=r.value: 
                    r.left.visited=True
                    q.enqueue(r.left)
                else: 
                    return False
                if r.right.value>r.value: 
                    r.right.visited=True
                    q.enqueue(r.right)
                else: 
                    return False

    def __init__(self):
        self.root=None   
    def add(self, node1):
        self.root.add(self.root, node1)

    def inorder_print(self, root):
        if root!=None: 
            self.inorder_print(root.left)
            #note that visiting is only for the core node
            # there are two recursive calls to left and right subtrees
            print(str(root.value))
            self.inorder_print(root.right)
        


def main():
    t=BST()
    node1=t.Node(10)
    t.root=node1
    node2=t.Node(5)
    node3=t.Node(15)
    node4=t.Node(3)
    node5=t.Node(7)
    node6=t.Node(13)
    node7=t.Node(19)
    node1.add(node1,node2)
    node1.add(node1,node3)
    node1.add(node1,node4)
    node1.add(node1,node5)
    node1.add(node1,node6)
    node1.add(node1,node7)
    print(t.inorder_print(t.root))
    nodeAdd=t.Node(6)
    node1.add(node1,nodeAdd)
    print(t.inorder_print(t.root))
    #print(str(t.root.left.value)+" "+str(t.root.value)+" "+str(t.root.right.value))


if __name__=="__main__":
    main()

       