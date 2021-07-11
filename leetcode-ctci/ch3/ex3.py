class SetOfStacks: 

    class Stack: 
        class Node: 
            def __init__(self, data, next):
                self.data=data
                self.next=next
            
        def __init__(self, capacity, next, index):
            self.top=None
            self.size=0
            self.min=None
            self.capacity=capacity
            self.next=next
            self.index=index

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

    def __init__(self):
        self.topS=None
        self.stackNum=1
        

    def push(self, d):
        if self.topS==None: 
            st=self.Stack(5, None, 0)
            self.topS=st
            newN=st.Node(d,st.top)
            st.top=newN
            st.size+=1
            self.stackNum+=1
            

        else: 
            current=self.topS
            current.size+=1
            if current.capacity<current.size: 
                newS=self.Stack(current.capacity, self.topS, (current.index+1))
                self.topS=newS
                newE=newS.Node(d,newS.top)
                newS.top=newE
                self.stackNum+=1    
            else: 
                newE=current.Node(d,current.top)
                current.top=newE

            
    def pop(self):
        current=self.topS
        current.size-=1
        self.stackNum-=1
        if current.top==None: 
            return None
        
        current.top=current.top.next
    
    def popAt(self, index):
        st=self.topS
        while(st!=None):
            if st.index==index: 
                d=st.top.data
                st.pop()
                return d
            st=st.next
        
    
    def print(self):
        t=self.topS
        index=0
        while(t!=None):
            print("stack"+str(index))
            t.print()
            print()
            index+=1
            t=t.next

        



        

def main(): 
    '''
    st=Stack(6)
    st.push(3)
    st.push(5)
    st.push(7)
    st.print()
    print("top is "+str(st.pop()))
    print("min is "+str(st.minI()))
    st.print()
    '''
    sets1=SetOfStacks()
    sets1.push(1)
    sets1.push(2)
    sets1.push(3)
    sets1.push(4)
    sets1.push(5)
    sets1.push(6)
    sets1.push(7)

    sets1.print()
    index=0
    print("popped data at index "+str(index)+" is "+str(sets1.popAt(index)))
    print("new stacks is ")
    sets1.print()


if __name__ == "__main__":
     main()
        
