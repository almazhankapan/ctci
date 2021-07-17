class DinnerPlates:
    class Stack:
        class Node:
            def __init__(self, val,next1):
                self.val=val
                self.next1=next1
        def __init__(self):
            self.top=None
            self.size=0
        
        def push(self, val):
            newN=self.Node(val, self.top)
            self.top=newN
            self.size+=1
        
        def pop(self):
            if self.top==None:
                return -1
            else:
                v=self.top.val
                self.top=self.top.next1
                self.size-=1
                return v
        def peek(self):
            if self.top==None:
                return -1
            else:
                v=self.top.val
                return v
        
        def print(self):
            h=self.top
            while(h!=None):
                print(str(h.val) +"=>",end="")
                h=h.next1
            print()
          
            
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.stacks=[]
        

    def push(self, val: int) -> None:
        if len(self.stacks)==0:
            st=self.Stack()
            st.push(val)
            self.stacks.append(st)
        else: 
            found=False
            i=0
            while(not found and i<len(self.stacks)):
                st=self.stacks[i]
                if (st.size==self.capacity): 
                    i+=1
                    found=False
                else: 
                    st.push(val)
                    found=True
                    return None
            if not found: 
                newSt=self.Stack()
                newSt.push(val)
                self.stacks.append(newSt)


            
        
    def pop(self) -> int:
        if len(self.stacks)==0:
            return -1
        else: 
            found=False
            i=len(self.stacks)-1
            while(i>=0 and not found):
                st=self.stacks[i]
                if st.peek()==-1:
                    found=False
                    i-=1
                else: 
                    found=True
                    v=st.pop()
                    return v
            if not found: 
                return -1 

            
        

    def popAtStack(self, index: int) -> int:
        #ind=len(self.stacks)-1-index
        if index>=len(self.stacks):
            return -1
        st=self.stacks[index]
        if st.top==None: 
            return -1
        else: 
            v=st.pop()
            return v

    def print(self):
        for x in self.stacks: 
            x.print()
            print()

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)  

'''
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[7],[8],[20],[21],[0],[2],[],[],[],[],[]]
'''
'''
["DinnerPlates","",,,"popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
[[2],[7],[9],[8],[1],[474],[216],[256],[196],[332],[43],[75],[22],[273],[101],[11],[403],[33],[365],[338],[331],[134],[1],[250],[19],[],[],[],[],[],[],[],[],[],[]]

'''
'''
def main():
    s=DinnerPlates(2)
    s.push(373)
    s.push(86)
    s.push(395)
    s.push(306)
    s.push(370)
    s.push(94)
    s.push(41)
    s.push(17)
    s.push(387)
    s.push(403)
    s.push(66)
    s.push(82)
    s.push(27)
    s.push(335)
    s.push(252)
    s.push(6)
    s.push(269)
    s.push(231)
    s.push(35)
    s.push(346)
    s.print()
    print("pop at 4")
    print(s.popAtStack(4))
    s.print()
    print(s.popAtStack(6))
    s.print()
    print(s.popAtStack(2))
    s.print()
    print(s.popAtStack(5))
    s.print()
    print(s.popAtStack(2))
    s.print()
    print(s.popAtStack(2))
    s.print()
'''
def main():
    s=DinnerPlates(1)
    s.push(1)
    s.push(2)
    s.push(3)
    s.print()
    print(s.popAtStack(1))
    s.print()
    print(s.pop())
    s.print()
    print(s.pop())
    s.print()
   
if __name__=="__main__":
    main()

        



