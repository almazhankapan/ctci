class BST: 
    class Node: 
        def __init__(self, value, left=None, right=None):
            self.value=value
            self.left=left
            self.right=right

        def inorder_print(self, root):
            if root!=None: 
                self.inorder_print(root.left)
                #note that visiting is only for the core node
                # there are two recursive calls to left and right subtrees
                print(str(root.value))
                self.inorder_print(root.right)
    
    def __init__(self):
        self.root=None
    '''
    steps: root is 2, left child becomes 1, right child becomes 3 and 2 is returned
    so, left iteration is finished and return 2 becomes left child of root
    ; then array is 5,6,7 and mini-root is 6;its left is 5,right is 7
    so right iteration is finished and returned 6 becomes root's right child
    '''
    def createMinBst(self, array):
        if array==None: 
            return None
        #base case--if only one node, create and return a node
        if len(array)==1:
            return self.Node(array[0])
        else: 
        #create subBST trees
            mid=int(len(array)/2)
            #note that it's not self.root - since there will be subroots and recursive calls
            #THE MOST IMPORTANT==ROOT IS THE NODE AT MID ARRAY/SUBARRAY
            root=self.Node(array[mid])
            left=self.createMinBst(array[:mid])
            right=self.createMinBst(array[mid+1:])
            root.left=left
            root.right=right
            #return root or subroot
            return root
def main():
    t=BST()
    t.root=t.createMinBst([1,2,3,4,5,6,7])
    t.root.inorder_print(t.root)



if __name__=="__main__":
    main()

