class Stack: 
    class MinStack: 
        class Node: 
            def __init__(self, value, next):
                self.value=value
                self.next=next

        def __init__(self):
            self.top=None
            self.min=None

        def push(self, value):
            newN=self.Node(value, self.top)
            self.top=newN

        def pop(self):
            v=self.top.value
            self.top=self.top.next
            return v

        def peek(self):
            v=self.top.value
            return v

    def __init__(self):
        self.top=None
        self.min=None
        self.minStack=self.MinStack()

    def push(self, value):
        newN=self.Node(value, self.top)
        self.top=newN
        if self.min==None: 
            self.min=newN
            self.minStack.push(newN.value)
        else: 
            if self.min.value>newN.value: 
                self.min=newN
                self.minStack.push(newN.value)

    def pop(self):
        v=self.top.value
        #retrieve the next min if top is min
        if self.minStack.head==self.top: 
            self.minStack.pop()
            self.min=self.minStack.head
        
        self.top=self.top.next
        return v

    def peek(self):
        v=self.top.value
        return v
    
    def min(self):
        return self.min


def main():
    s=Stack()
    s.push(4)
    s.push(3)
    s.push(6)
    s.push(2)
    
    s.print()
    s.pop()
    s.print()
   



if __name__=="__main__":
    main()



