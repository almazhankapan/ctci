class SetOfStacks: 
    class Stack: 
        class Node: 
            def __init__(self, value, next):
                self.value=value
                self.next=next
        
        def __init__(self, next, index):
            self.top=None
            self.size=0
            self.next=next
            self.index=index
        
        def push(self, value):
            n=self.Node(value, self.top)
            self.size+=1
            self.top=n
        
        def pop(self) :
            d=self.top.value
            self.top=self.top.next
            self.size-=1
            return d

        def print(self):
            s=self.top
            while(s!=None):
                print(str(s.value)+"->",end="")
                s=s.next
            print()

    def __init__(self, thresh):
        self.topS=self.Stack(None, 0)
        self.thresh=thresh
    
    def push(self, value):
        if (self.topS).size==self.thresh: 
            newSt=self.Stack(self.topS, ((self.topS.index)+1))
            self.topS=newSt
            newSt.push(value)
        else: 
            self.topS.push(value)
    
    def pop(self):
        d=(self.topS).pop()
        if (self.topS).size==0:
            self.topS=(self.topS).next
        return d
    
    def popAt(self, i):
        index=0
        current=self.topS
        if i==0:
            d=self.topS.pop()
            return d
        while(index!=i):
            current=current.next
            index+=1
        d=current.pop()
        return d
    
    def print(self):
        top=self.topS
        while(top!=None):
            top.print()
            top=top.next


def main():
    set1=SetOfStacks(2)
    set1.push(1)
    set1.push(2)
    set1.push(3)
    set1.push(4)
    set1.push(5)
    set1.push(7)
    set1.print()
    print("popped: "+str(set1.popAt(1)))
    set1.print()

if __name__ == "__main__":
    main()

        
        
        

        

