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

    

def reverse(ll):
    current=ll.head
    previous=None
    next=None
    while(current!=None):
        next=current.next
        current.next=previous
        #Note!!--to make references correctly in python, 
        #you need to actually assign values
        if previous!=None: 
            current.next.value=previous.value
        previous=current
        if current!=None: 
            previous.value=current.value
        current=next
        if next!=None: 
            current.value=next.value #move one step 
    ll.head=previous
    if previous!=None: 
        ll.head.value=previous.value
    return ll

        

def main():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.print()
    newl=reverse(ll)
    newl.print()
   

if __name__=="__main__":
    main()


    