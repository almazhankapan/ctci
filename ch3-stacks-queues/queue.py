class Queue: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self, value):
        newN=self.Node(value, None)
        self.tail.next=newN
        self.tail=newN

    def pop(self):
        v=self.head.value
        self.head=self.head.next
        return v
    
    def peek(self):
        v=self.head.value
        return v