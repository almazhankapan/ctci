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

    def isPalindrome(self):
        h=self.head
        buff=[]
        while(h!=None):
            buff.append(h.value)
            h=h.next

        mid=int(len(buff)/2)
        if len(buff)%2==0:
            first=buff[0:mid]
            second=list(reversed(buff[mid:len(buff)]))
        else: 
            first=buff[0:mid]
            second=list(reversed(buff[(mid+1):len(buff)]))
        if first==second: 
            return True
        else: 
            return False

        
        


def main():
    ll=LinkedList()
    ll.insert(3)
    ll.insert(7)
    ll.insert(9)
    ll.insert(9)
    ll.insert(7)
    ll.insert(3)
    ll.print()
    print(ll.isPalindrome())
    ll2=LinkedList()
    ll2.insert(3)
    ll2.insert(7)
    ll2.insert(9)
    ll2.insert(11)
    ll2.insert(9)
    ll2.insert(7)
    ll2.insert(3)
    ll2.print()
    print(ll2.isPalindrome())
    ll3=LinkedList()
    ll3.insert(3)
    ll3.insert(7)
    ll3.insert(8)
    ll3.insert(11)
    ll3.insert(9)
    ll3.insert(7)
    ll3.insert(3)
    ll3.print()
    print(ll3.isPalindrome())
   

if __name__=="__main__":
    main()


    