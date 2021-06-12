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
        print()

    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.size==0

def sort(old): 
    new=Stack()
    #we are first sorting in ascending -- largest is top
    while(not new.isEmpty()):
        tmp=old.pop()
        #we are transfering from old to placeholder
        #pop from new and push back to old
        while((not new.isEmpty()) and new.peek()>tmp ):
            old.push(new.pop())
        new.push(tmp) 
    #we are sorting back into descending - smallest is top
    while(not new.isEmpty()):
        old.push(new.pop())

def sort1(stack):
    tempSt=Stack()
    while(not stack.isEmpty()):
        tmp=stack.pop()
        while(not tempSt.isEmpty() and (tmp>tempSt.peek())):
            stack.push(tmp)
        tempSt.push(tmp)
    while(not tempSt.isEmpty()):
        stack.push(tempSt.pop())

def main(): 
    st=Stack()
    st.push(3)
    st.push(5)
    st.push(7)
    st.push(2)
    st.push(6)
    st.print()
    sort(st)
    st.print()




if __name__ == "__main__":
     main()
        
