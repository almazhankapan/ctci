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
    
    

def main(): 
    st=Stack()
    st.push(3)
    st.push(5)
    st.push(7)
    st.print()
    print("top is "+str(st.pop()))
    print("min is "+str(st.minI()))
    st.print()



if __name__ == "__main__":
     main()
        
