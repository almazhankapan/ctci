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

def sumLists(ll1,ll2):
    '''
    1234-->4321
    2378-->8732

    3 5 0 13-->13 0 5 3
    '''
    
    h1=ll1.head
    h2=ll2.head
    carry=0
    if h1==None and h2!=None: 
        return ll2
    if h2==None and h1!=None: 
        return ll1
    if h1==None and h2==None: 
        return None
    sumH=None
    sumL=LinkedList()
    while(h1!=None and h2!=None):
        sum1=h1.value+h2.value+carry
        if sum1>10:
            carry=1
            sum1=sum1%10
        else: 
            carry=0
        sumL.insert(sum1)
        h1=h1.next
        h2=h2.next
    
    if carry==1:
        sumL.insert(1)

    return sumL





def main():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(7)
    ll.insert(9)
    ll.insert(9)
    ll.print()
    ll2=LinkedList()
    ll2.insert(4)
    ll2.insert(5)
    ll2.insert(6)
    ll2.insert(5)
    ll2.print()
    newl=sumLists(ll, ll2)
    newl.print()

if __name__=="__main__":
    main()


    
