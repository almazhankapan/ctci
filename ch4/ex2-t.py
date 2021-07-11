
class Node: 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.visited=False
    
    def add_child(self, Node):
        if self.left!=None: 
            self.right=Node
        else: 
            self.left=Node

    
def createMinBST(arr):
    #array with elements in an increasing order
    #adding middle as root and adding the rest as left and right substrees
    #use inorder? 
    mid_index=int(len(arr)/2)
    elements=1
    root=Node(arr[mid_index])
    while(elements!=len(arr)):
        root.left=arr[mid_index-1]
        root=arr[mid_index]    
        root.right=arr[mid_index+1]
    
        

    