class Stack: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.head=None
    
    def push(self, value):
        newN=self.Node(value, self.head)
        self.head=newN
    
    def pop(self):
        if self.head==None: 
            return None
        else: 
            v=self.head
            self.head=self.head.next
            return v
    
    def isEmpty(self):
        return self.head==None
    
    def peek(self):
        if self.head==None: 
            return None
        else: 
            v=self.head
            return v

    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value) +"=>",end="")
            h=h.next
        print()




def main():

    s=Stack()
    s.push(4)
    s.push(3)
    s.push(6)
    s.push(2)
    
    s.print()
    s.pop()
    s.print()
   



if __name__=="__main__":
    main()



