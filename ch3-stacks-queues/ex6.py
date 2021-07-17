class AnimalShelter: 
    class Node: 
        def __init__(self, value, next1):
            self.value=value
            self.next1=next1
    def __init__(self) :
        self.head=None
        self.tail=None
    
    def enqueue(self, value):
        newN=self.Node(value, None)
        if self.tail==None: 
            self.head=newN
            self.tail=newN
        else:  
            self.tail.next1=newN
            self.tail=newN
    def dequeueAny(self):
        if self.head==None: 
            return None
        else: 
            v=self.head.value
            self.head=self.head.next1
            return v

    def dequeueCat(self):
        return self.dequeueAnimal("cat")
    
    def dequeueDog(self):
        return self.dequeueAnimal("dog")

    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value) +"=>",end="")
            h=h.next1
        print()

    def dequeueAnimal(self, ani):
        if self.head==None: 
            return None
        else: 
            h=self.head
            if h.value==ani:
                v=self.head.value
                self.head=self.head.next1
                return v
            else: 
                found=False
                while(h.next1!=None):
                    if h.next1.value==ani:
                        found=True
                        break
                    else: 
                        h=h.next1
                if found: 
                    h.next1=(h.next1).next1
                    return ani

                else: 
                    return -1
            
    
    def peek(self):
        if self.head==None: 
            return None
        else: 
            v=self.head.value
            return v
    
def main():
    s=AnimalShelter()
    s.enqueue("cat")
    s.enqueue("cat")
    s.enqueue("dog")
    s.enqueue("cat")
    s.enqueue("dog")
    s.print()
    print(s.dequeueAny())
    s.print()
    print(s.dequeueDog())
    s.print()




if __name__=="__main__":
    main()      
 
