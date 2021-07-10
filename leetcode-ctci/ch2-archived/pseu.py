class LinkedList: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=next
    def __init__(self):
        self.count=0
        self.head=None
    
    def insert(self, value):
        new=self.Node(value, None)
        n=self.head
        if n==None: 
            self.head=new
        else: 
            while(n.next!=None):
                n=n.next
            n.next=new
            self.count+=1
    
    def delete(self, value):
        h=self.head
        if h.value==value: 
            self.head=self.head.next
        while(h.next.value!=value):
            h=h.next
        h.next=h.next.next
        self.count-=1

    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value)+"=>",end="")
            h=h.next
        print()

    #doesnt work if 355556 etc
    def removeDup(self):
        map1={}
        h=self.head
        map1[h.value]=1
        while(h.next!=None):
            if h.next.value in map1.keys():
                h.next=h.next.next
                h=h.next
            else: 
                map1[h.next.value]=1
                h=h.next
    
    def findKth(self, k):
        h=self.head
        h2=self.head
    
        while(k!=0):
            k-=1
            h=h.next
        
        while(h!=None):
            h2=h2.next
            h=h.next
        
        return h2.value
    
    def findMid(self):
        h=self.head
        h2=self.head
        length=0
        while (h!=None):
            h=h.next
            length+=1
        mid=int(length/2)
        count=0
        while(count!=mid):
            h2=h2.next
            count+=1
            if count==mid: 
                return h2
    
    def partition(self, x):
        h=self.head
        h2=h
        smaller=None
        s=None
        larger=None
        l=larger
        while(h!=None):
            if h.value<x:
                if smaller==None: 
                    smaller=self.Node(h.value, None)
                    s=smaller
                    h=h.next
                else: 
                    smaller.next=self.Node(h.value, None)
                    smaller=smaller.next
            else: 
                if larger==None: 
                    larger=self.Node(h.value, None)
                    h=h.next
                    l=larger
                else: 
                    larger.next=self.Node(h.value, None)
                    larger=larger.next
            h=h.next

        if smaller==None: 
            self.head=l
        if larger==None: 
            self.head=s
        else: 
            smaller.next=l
            self.head=s
    
        

def deleteMid(node):
    node.value=node.next.value
    node.next=node.next.next



def main():
    list1=LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(3)
    list1.insert(4)
    list1.insert(4)
    list1.insert(5)
    list1.insert(1)
    list1.insert(7)
    list1.insert(8)
    list1.print()
    list1.removeDup()
    list1.print()
    #print(list1.findKth(3))
    print(list1.findMid().value)
    deleteMid(list1.findMid())
    list1.print()
    list2=LinkedList()
    list2.insert(2)
    list2.insert(1)
    list2.insert(5)
    list2.insert(4)
    list2.insert(6)
    list2.insert(5)
    list2.insert(3)
    list2.print()
    list2.partition(4)
    list2.print()
if __name__ =="__main__": 
    main()





        
        
