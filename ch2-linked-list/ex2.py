
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



def lastKth(ll, k):
    h1=ll.head
    h2=ll.head
    #123457
    #3457
    i=1
    while(i!=k):
        h1=h1.next
        i+=1
    
    while(h1.next!=None):
        h2=h2.next
        h1=h1.next
    
    return h2.value

def main():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.print()
    print(lastKth(ll, 2))
    print(lastKth(ll, 4))

if __name__=="__main__":
    main()