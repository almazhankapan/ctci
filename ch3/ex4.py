class MyQueue: 
    class Stack: 
        class Node: 
            def __init__(self, data, next):
                self.data=data
                self.next=next
        
        def __init__(self):
            self.top=None
            self.size=0
            self.min=None

        def minI(self):
            return self.min.data

        def push(self, data):
            newN=self.Node(data, self.top)
            if (self.min==None): 
                self.min=newN
            elif self.min.data>newN.data: 
                self.min=newN
            self.top=newN
            self.size+=1
        
        def isEmpty(self):
            return self.size==0

        def pop(self) :
            if self.top==None: 
                return None
            d=self.top.data
            self.top=self.top.next
            self.size-=1
            return d
    
        def print(self):
            t=self.top
            while(t!=None):
                print(str(t.data)+"->",end="")
                t=t.next
    
    def __init__(self):
        self.stackNew=self.Stack()
        self.stackOld=self.Stack()
        self.topQ=self.stackOld.top
        self.size=self.stackNew.size+self.stackOld.size
    
    def getsize(self):
        return self.stackNew.size
    
    def push(self, data):
        self.stackNew.push(data)

    def pop(self):
        #stackOld contains reverse of the stack new which is a usual stack
        #stackold popped from head
        #stack new -- inserted to tail
        while(not self.stackNew.isEmpty):
            self.stackOld.push(self.stackNew.pop())
        
        self.stackOld.pop()


    
        
        
        
            
        
    
        
    