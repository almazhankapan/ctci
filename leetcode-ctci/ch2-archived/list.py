class Node: 
    def __init__(self, data, next):
        self.data=data
        self.next=next
    

class LinkedList: 
    def __init__(self):
        self.head=None #important--you don't set head, but you do specify that it's none
    
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


def main(): 
    list=LinkedList()
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.delete(4)
    list.print()

if __name__ == "__main__":
    main()
