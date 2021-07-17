class MyQueue:
    class Stack:
        class Node:
            def __init__(self, value,next1):
                self.value=value
                self.next1=next1
        
        def __init__(self):
            self.top=None
                
        def push(self, x):
            newN=self.Node(x,self.top)
            self.top=newN
        def print(self):
            h=self.top
            while(h!=None):
                print(str(h.value) +"=>",end="")
                h=h.next1
            print()
        
        def pop(self):
            if self.top==None:
                return None
            else:
                v=self.top.value
                self.top=self.top.next1
                return v
        
        def peek(self):
            if self.top==None:
                return None
            else:
                return self.top.value
        
        def empty(self):
            return self.top==None
            
                
    def __init__(self):
        self.head=None
        self.tail=None
        self.stackH=self.Stack()
        self.stackE=self.Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackH.push(x)
        self.tail=self.stackH.top
    
    def reverse(self):
        if self.stackE.empty():
            stack=self.stackH
            while(not stack.empty()):
                self.stackE.push(stack.pop())
            self.stackH=stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.reverse()
        v=self.stackE.pop()
        self.head=self.stackE.top
        return v
        
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.reverse()
        v=self.stackE.peek()
        return v
    
    def print(self):
        self.reverse()
        self.stackE.print()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stackE.empty():
            self.reverse()
            return self.stackE.empty()
        else:     
            return self.stackE.empty()
        
def main():
    s=MyQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.print()
    print(s.pop())
    s.print()
    s.push(5)
    s.print()
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())



   
   



if __name__=="__main__":
    main()      


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()