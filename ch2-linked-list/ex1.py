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
    
def removeDup(ll):
    h=ll.head
    newll=LinkedList()
    h1=None
    map1={}
    while(h!=None):
        if h.value in map1:
            h=h.next
        else: 
            map1[h.value]=1
            newll.insert(h.value)
            if newll.head.next==None: 
                h1=newll.head
            h=h.next
    newll.head=h1
    return newll

    
def removeDup2(ll):
    h=ll.head
    h1=ll.head
    previous=None
    map1={}
    #123445666
    while(h!=None):
        if h.value in map1:
            previous.next=h.next
            h=h.next
        else: 
            map1[h.value]=1
            previous=h
            h=h.next
    ll.head=h1
    return ll


def main():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(3)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.insert(5)
    ll.print()
    newl=removeDup(ll)
    newl.print()

if __name__=="__main__":
    main()


    
