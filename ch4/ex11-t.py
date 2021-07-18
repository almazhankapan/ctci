import random
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.size = 1
        if self.left:
          self.size += self.left.size
        if self.right:
          self.size += self.right.size
    
    def get_random(self):
        self.helper(random(0, self.size - 1))
        
    def helper(self, rand):
        if rand == 0:
            return self
        
        if self.left:
            if rand-1 < self.left.size:
                return self.left.helper(rand-1)
            elif self.right:
                return self.right.helper(rand-1-self.left.size)
        
        if self.right:
            return self.right.helper(rand-1)
            
        return None

