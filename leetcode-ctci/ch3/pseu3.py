class Stack: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.top=None
        self.min=None
        self.mins=[]
    
    def push(self, value):
        #for stack it's a<-b<-c<-top<-newtop
        n=self.Node(value, self.top)
        self.top=n
        if self.min==None: 
            self.min=value
            self.mins.append(value)
        elif value<self.min: 
            self.min=value
            self.mins.append(value)

        
        
        
    
    def pop(self):
        d=self.top.value
        if d==self.min:  
            self.mins=self.mins[0:(len(self.mins)-1)]
            self.min=self.mins[len(self.mins)-1]
        self.top=self.top.next
        return d
    
    def min(self):
        return self.min
def stacks():
    st=Stack()
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(6)
    st.push(6)
    st.push(7)
    st.push(1)
    print("min"+str(st.min))
    print(st.pop())
    print(str(st.min))

class Queue: 
    class Node: 
        def __init__(self, value, next) :
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
        self.tail=None
        
    def push(self, value):
        n=self.Node(value,None )
        if self.head==None: 
            self.head=n
        if self.tail==None: 
            self.tail=n
        else: 
            self.tail.next=n
            self.tail=n
    def pop(self):
        d=self.head.value
        self.head=self.head.next
        return d   

    def print(self):
        cur=self.head
        while(cur!=None):
            print(str(cur.value)+"->",end="")
            cur=cur.next
        print()

def main():
    #stacks()
    q=Queue()
    q.push(1)
    q.push(2)
    q.push(2)
    q.print()
    print(q.pop())
    q.print()

if __name__=="__main__":
    main()