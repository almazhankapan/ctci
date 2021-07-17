class MinStack:
    class Stack:
        class Node:
            def __init__(self,val,next1):
                self.val=val
                self.next1=next1
            
        def __init__(self):
            self.head=None
        
        def push(self, val: int) -> None:
            newN=self.Node(val,self.head)
            self.head=newN
        
        def pop(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                self.head=self.head.next1
                return h
        
        def peek(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                return h
                
            
           
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins=[]
        self.stack=self.Stack()
        
        
        

    def push(self, val: int) -> None:
        self.stack.push(val)
        if len(self.mins)==0:
            self.mins.append(val)
        elif self.mins[-1]>val:
            self.mins.append(val)
        else: 
            self.mins.append(self.mins[-1]) 
            

    def pop(self) -> None:
        v=self.stack.pop()
        self.mins.pop()
        return v

    def top(self) -> int:
        return self.stack.peek()
        

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()