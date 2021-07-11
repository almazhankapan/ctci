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
    
def detectLoop(ll):
    slower=ll.head
    faster=ll.head.next
    while(slower!=None and faster!=None and faster.next!=None):
        if slower==faster: 
            return True
        else: 
            slower=slower.next
            faster=faster.next.next
    return False




def main():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ss=LinkedList.Node(5,ll.head)
    ll.head.next=ss
    print(detectLoop(ll))

if __name__=="__main__":
    main()


    
