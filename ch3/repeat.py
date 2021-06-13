class Stack: 
    class Node: 
        def __init__(self, data, next):
            self.data=data
            self.next=next
        
    def __init__(self):
        self.top=None
        self.size=0
    
    def push(self, d):
        new=self.Node(d,self.top) 
        self.top=new
        self.size+=1
    
    def pop(self) :
        if self.top==None: 
            return None
        d=self.top.data
        self.top=self.top.next
        self.size-=1
        return d

    def isEmpty(self):
        return (self.size==0)
    
    def peek(self):
        return self.top.data

    def print(self):
        cur=self.top
        while(cur!=None):
            print(str(cur.data)+"-", end="")
            cur=cur.next
        print()

def sort(st):
    st2=Stack()
    while(not st.isEmpty()):
        temp=st.pop()
        #top of newstack should be smaller than temp value
        while(not st2.isEmpty() and (st2.peek()>temp) ):
            st.push(st2.pop())#we push temp value
        st2.push(temp)

    while(not st2.isEmpty()):
        st.push(st2.pop())

def sort1(stack):
    st2=Stack()
    while(not stack.isEmpty()):
        tmp=stack.pop()
        while(not st2.isEmpty() and st2.peek()>tmp):
            stack.push(st2.pop())
        st2.push(tmp)

    while(not st2.isEmpty()):
        stack.push(st2.pop())

def main(): 
    st=Stack()
    st.push(3)
    st.push(5)
    st.push(7)
    st.push(2)
    st.push(6)
    st.print()
    sort1(st)
    st.print()
    print(st.top.data)


if __name__ == "__main__":
     main()
        
