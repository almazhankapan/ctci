class Stack: 
    class Node: 
        def __init__(self, data, next):
            self.data=data
            self.next=next
    
    def __init__(self):
        self.top=None
        self.size=0
        self.min=None
    
    def min(self):
        return self.min
    
    def isEmpty(self):
        return self.size==0
    
    def length(self):
        return self.size
    
    def insert(self,  d):
        newN=self.Node(d,self.top)
        self.top=newN
        self.size+=1
    
    def pop(self):
        if self.top==None: 
            return None
        else: 
            d=self.top.data
            self.top=self.top.next
            self.size-=1
            return d
    
    def peek(self):
        return self.top.data
    
    def print(self):
        t=self.top
        while(t!=None):
            print(str(t.data)+"->",end="")
            t=t.next
        print()


class Stack: 
    class Node: 
        def __init__(self, data, next):
            self.data=data
            self.next=next
    
    def __init__(self):
        self.top=None
        self.size=0
    
    def isEmpty(self):
        return self.size==0
    
    def length(self):
        return self.size
    
    def insert(self,  d):
        newN=self.Node(d,self.top)
        self.top=newN
        self.size+=1
    
    def pop(self):
        if self.top==None: 
            return None
        else: 
            d=self.top.data
            self.top=self.top.next
            self.size-=1
            return d
    
    def peek(self):
        return self.top.data
    
    def print(self):
        t=self.top
        while(t!=None):
            print(str(t.data)+"->",end="")
            t=t.next
        print()

class Queue: 
    class Node: 
        def __init__(self, data, next):
            self.data=data
            self.next=next
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def isEmpty(self):
        return self.size==0
    
    def length(self):
        return self.size
    
    def insert(self,  d):
        newN=self.Node(d,None)
        if self.tail==None: 
            self.head=self.tail=newN
            self.size+=1
        else: 
            self.tail.next=newN
            self.tail=newN
            self.size+=1
    
    def pop(self):
        if self.head==None: 
            return None
        else: 
            d=self.head.data
            self.head=self.head.next
            self.size-=1
            return d
    
    def peek(self):
        return self.head.data
    
    def print(self):
        t=self.head
        while(t!=None):
            print(str(t.data)+"->",end="")
            t=t.next
        print()
def main():
    print("stack")
    st=Stack()
    st.insert(2)
    st.insert(3)
    st.insert(7)
    st.print()
    print("top: "+str(st.peek()))
    st.pop()
    st.print()

    print("queue")
    q=Queue()
    q.insert(2)
    q.insert(3)
    q.insert(7)
    q.print()
    print("top: "+str(q.peek()))
    q.pop()
    q.print()

if __name__ == "__main__":
     main()
 


