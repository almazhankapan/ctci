# enqueue-to the end
# dequeue=from the head

class MyQueue: 
    class Stack:
        class Node:
            def __init__(self,val,next):
                self.val=val
                self.next=next
        def __init__(self):
            self.head=None
        
        def push(self, val: int) -> None:
            newN=self.Node(val,self.head)
            self.head=newN
            
        def pop(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                self.head=self.head.next
                return h

        def peek(self):
            if self.head==None:
                return None
            else:
                h=self.head.val
                return h
        def isEmpty(self):
            return self.head==None

        def print(self):
            h=self.head
            while(h!=None):
                print(str(h.val) +"=>",end="")
                h=h.next
            print()

    def __init__(self):
        self.stackH=self.Stack()
        self.stackE=self.Stack()
        self.head=None
        self.tail=None

    def enqueue(self, val):
        self.stackH.push(val)
        self.tail=self.stackH.head

    def reverse1(self):
        while(not self.stackH.isEmpty()):
            if self.stackH.peek() != None: 
                self.stackE.push(self.stackH.pop())
        return self.stackE
        
    def dequeue(self):
        self.reverse1()
        v=self.stackE.pop()
        self.head=self.stackE.head
        return v
    
    def print(self):
        if self.stackE.head==None: 
            s=self.stackH
        else: 
            s=self.stackE
        s.print()


def main():
    s=MyQueue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    s.print()
    print("tail is"+str(s.tail.val))
    print(s.dequeue())
    s.print()
    print("head is"+str(s.head.val))



   
   



if __name__=="__main__":
    main()      
