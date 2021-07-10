class Node: 
    def __init__(self, data, next):
        self.data=data
        self.next=next
    

class LinkedList: 
    def __init__(self):
        self.head=None #important--you don't set head, but yo
    
    def insert(self, data):
        new=Node(data, None)
        if self.head==None: 
            self.head=new
        else: 
            node=self.head
            while(node.next!=None):
                node=node.next
            node.next=new
    
    def delete(self, data):
        node=self.head
        if node==None: 
            return -1
    
        else: 
            while((node.next).data!=data):
                node=node.next
        
            if (node.next).data==data: 
                node.next=node.next.next
                return 1
            else: 
                return -1

    def print(self):
        node=self.head
        while(node!=None):
            print(str(node.data) + "=>",end="")
            node=node.next

def getData(list, str1,node):
    sum=str1
    if node.next==None: 
        sum=node.data
        return sum
    else: 
        sum+=getData(list, sum, node.next)
        sum+=node.data
        
    return sum

def reverseList(list):
    prev=None
    current=list.head
    # a b c None--> prev=None, current=a,next=b,a.next=None, prev=a,current=b
    while(current!=None):
        next=current.next
        current.next=prev #reverse prev and current.next
        prev=current #move pointer to the right
        current=next #move pointer to the right
    list.head=prev
        

def main(): 
    list1=LinkedList()
    list1.insert(4)
    list1.insert(5)
    list1.insert(2)
    list1.insert(7)
    list1.print()
    print()
    print(getData(list1,"",list1.head))
    list1.print()

if __name__ == "__main__":
    main()