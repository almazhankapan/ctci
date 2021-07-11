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


def intersect(ll1,ll2):
    h1=ll1.head
    h2=ll2.head
    count1=count2=0
    while(h1.next!=None):
        count1+=1
        h1=h1.next
    count1+=1

    while(h2.next!=None):
        count2+=1
        h2=h2.next
    if h1!=h2:
        return False
    diff=0
    if count1!=count2:
        if count1>count2:
            hh=ll1.head
            hh2=ll2.head
            diff=count1-count2
        else: 
            hh=ll2.head
            hh2=ll1.head
            diff=count2-count1
    
    while(diff!=0):
        hh=hh.next
    
    while(hh!=None):
        if hh==hh2:
            return True
        else: 
            hh=hh.next
            hh2=hh2.next

    
    
        
    

    
        

        
        


def main():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(4)
    ll.insert(5)
    ll.print()
    ll2=LinkedList()
    ll2.insert(3)
    ll2.insert(7)
    ll2.insert(9)
    ll2.insert(11)
    ll2.print()
    print(intersect(ll,ll2))
   

if __name__=="__main__":
    main()


    