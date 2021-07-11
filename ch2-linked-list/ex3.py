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
    
    def findMiddle(self):
        h=self.head
        h1=self.head
        count=0
        while(h!=None):
            count+=1
            h=h.next
        mid=int(count/2)

        count=0
        while(count!=mid):
            h1=h1.next
            count+=1

        return h1

    def deleteMid(self, node):
        if node.next==None: 
            node=None
        else: 
            newv=node.next.value
            node.value=newv
            node.next=node.next.next

    


def main():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.print()
    mid=ll.findMiddle()
    print("mid: "+str(mid.value))
    ll.deleteMid(mid)
    ll.print()

if __name__=="__main__":
    main()