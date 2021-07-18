class Node: 
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        self.visited=False
    #insert in binary tree should be breadth first sear
    def checkBalanced(self, node, left_lenght, right_lenght, diff):
        '''
           5
        1      5
    3     6   7     9
                55        22
                    88        2223
        '''
        if self.left!=None: 
            self.checkBalanced(node.left, left_lenght+1,0)
        else: 
            if self.right!=None: 
                diff+=1
        if self.right!=None: 
            self.checkBalanced(node.right, 0,right_lenght+1)
        else: 
            if self.right!=None: 
                diff+=1

