class LinkedList: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    
    def __init__(self):
        self.head=None
    
    def insert(self, value):
        newN=self.Node(value, None)
        h=self.head
        if h==None: 
            self.head=newN
        else: 
            while(h.next!=None):
                h=h.next
            h.next=newN
    
    def delete(self, value):
        h=self.head
        if h.value==value: 
            self.head=self.head.next
        else: 
            while(h.next.value!=value):
                h=h.next
            h.next=h.next.next

    def print(self):
        h=self.head
        while h!=None: 
            print(str(h.value)+"->",end="")
            h=h.next
        print()

def partition(ll, x):
    larger=LinkedList()
    smaller=LinkedList()
    largerH=None
    h=ll.head
    while(h!=None):
        if h.value<x:
            smaller.insert(h.value)
            h=h.next
        if h.value>=x:
            larger.insert(h.value)
            h=h.next
            if larger.head.next==None: 
                largerH=larger.head
    s=smaller.head
    while(s.next!=None):
        s=s.next
    s.next=largerH

    return smaller


def main():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(7)
    ll.insert(0)
    ll.insert(9)
    ll.insert(2)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.insert(5)
    ll.print()
    newl=partition(ll, 4)
    newl.print()

if __name__=="__main__":
    main()


    
