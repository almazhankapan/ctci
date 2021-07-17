class SetOfStacks: 
    class Stack:
        class Node:
            def __init__(self,val,next):
                self.val=val
                self.next=next

        def __init__(self, thresh, next):
            self.head=None
            self.size=0
            self.thresh=thresh
            self.next=next

        def push(self, val: int) -> None:
            newN=self.Node(val,self.head)
            self.head=newN
            self.size+=1

        def pop(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                self.head=self.head.next
                self.size-=1
                return h

        def peek(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                return h

        def print(self):
            h=self.head
            while(h!=None):
                print(str(h.val) +"=>",end="")
                h=h.next
            print()


    def __init__(self, thresh):
        self.stacks=[]
        self.head=self.Stack(thresh, None)
        self.thresh=thresh
        self.stacks.append(self.head)
    
    def push(self, val):
        if self.head.size==self.head.thresh: 
            newS=self.Stack(self.thresh, self.head)
            newS.push(val)
            self.stacks.append(newS)
            self.head=newS
            
        else: 
            self.head.push(val)

    def pop(self):
        if self.head.size==0:
            return None
        else: 
            return self.head.pop()
    
    def popAt(self, i):
        st=self.stacks[i]
        return st.pop()
    
    def peek(self):
        if self.head.size==0:
            return None
        else: 
            return self.head.peek()

    def print(self):
        st=self.head
        while(st!=None):
            st.print()
            print()
            st=st.next
def main():
    s=SetOfStacks(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.print()
    '''
    s.pop()
    s.print()
    s.push(6)
    s.push(1)
    s.push(4)
    print("Final: ")
    s.print() 
    i=2
    s.popAt(len(s.stacks)-1-i)
    print("after popping at 1: ")
    s.print()
    '''

    
    
   
   
   



if __name__=="__main__":
    main()

        



