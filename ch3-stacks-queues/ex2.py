class MinStack: 
    #key is that MinStack class contains a stack subclass
    #but is not a stack itself--its rather a wrapper for stack subclass
    # and push, pop are made through push, pop calls to the stack subclass;
    # minstack has mins array which tracks local min element for each stack element
    class Stack: 
        class Node: 
            def __init__(self, value, next):
                self.value=value
                self.next=next
        def __init__(self):
            self.head=None

        def push(self, value):
            newN=self.Node(value, self.head)
            self.head=newN
    
        def pop(self):
            if self.head==None: 
                return None
            else: 
                v=self.head
                self.head=self.head.next
                return v

        def isEmpty(self):
            return self.head==None

        def peek(self):
            if self.head==None: 
                return None
            else: 
                v=self.head
                return v
    def __init__(self):
        self.minstack=self.Stack()
        self.mins=[]
    
    def push(self, value):
        self.minstack.push(value)
        if len(self.mins)==0:
            self.mins.append(value)
        else: #track local min
            if self.mins[-1]>value: 
                self.mins.append(value)
            else: 
                self.mins.append(self.mins[-1])
    
    def pop(self):
        v=self.minstack.pop()
        self.mins.pop()
    
    def isEmpty(self):
        return self.minstack.isEmpty()
    
    def peek(self):
        return self.minstack.peek()
    
    def getmin(self):
        return self.mins[-1]

    def print(self):
        h=self.minstack.head
        while(h!=None):
            print(str(h.value) +"=>",end="")
            h=h.next
        print()
    
    
    




def main():

    s=MinStack()
    s.push(4)
    s.push(7)
    s.push(3)
    s.push(2)
    s.push(5)
    print(s.getmin())
    s.print()
    s.pop()
    s.print()
    print(s.getmin())
    s.pop()
    s.print()
    print(s.getmin())
   



if __name__=="__main__":
    main()

