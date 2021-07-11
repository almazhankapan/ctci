class QueueSets: 
    class Stack: 
        class Node: 
            def __init__(self, value, next):
                self.value=value
                self.next=next

        def __init__(self):
            self.top=None
            self.len=0

        def push(self, value):
           n=self.Node(value, self.top)
           self.top=n
           self.len+=1
        
        def pop(self):
            d=self.top.value
            self.top=self.top.next
            self.len-=1
            return d
        
        def print(self):
            h=self.top
            while(h!=None):
                print(str(h.value)+"->",end="")
                h=h.next
            print()
        
        def isEmpty(self):
            return self.len==0
            

    def __init__(self):
        self.st1=self.Stack() 
        self.st2=self.Stack()  
        self.head=None
        self.end=None

    def push(self, value):
        self.st1.push(value)

    def pop(self):
        c=self.st1.top
        while(not self.st1.isEmpty()):
            self.st2.push(self.st1.pop())
            
        
        self.st2.pop()

        h=self.st2.top
        while(h!=None and not self.st2.isEmpty()):
            self.st1.push(self.st2.pop())
    
    def print(self):
        self.st1.print()

    
def main():
    #stacks()
    q=QueueSets()
    q.push(1)
    q.push(2)
    q.push(2)
    q.push(3)
    q.push(5)
    q.print()
    print(q.pop())
    q.print()

if __name__=="__main__":
    main()