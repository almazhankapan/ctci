class Queue: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next

    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self, value):
        newN=self.Node(value, None)
        if self.tail==None and self.head==None: 
            self.tail=newN 
            self.head=newN 
        else: 
            self.tail.next=newN
            self.tail=newN
    
    def dequeue(self):
        if self.head==None: 
            return None
        else: 
            v=self.head
            self.head=self.head.next
            return v

    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value)+"=>",end="")
            h=h.next
        print()
    
    def peek(self):
        if self.head==None: 
            return None
        else: 
            v=self.head
            return v


def main():

    q=Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(6)
    q.enqueue(2)
    
    q.print()
    q.dequeue()
    q.print()
   



if __name__=="__main__":
    main()