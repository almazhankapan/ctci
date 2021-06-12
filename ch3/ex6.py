class Queue: 
    class Node: 
        def __init__(self, time, animal, next):
            self.time=time
            self.animal=animal
            self.next=next
    #for stack: newN-->node-->node
    #for heap: head->node->node->tail 
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
               
    def enqueue(self, time, animal):
        newN=self.Node(time, animal,None)

        if self.tail==None: 
            self.tail=newN
        
        if self.head==None: 
            self.head=newN
        
        self.tail.next=newN
        self.tail=newN
        

    def dequeueAny(self):
        if self.head==None: 
            return None
        else: 
            d=self.head
            self.head=self.head.next
            return d
    

    def dequeueCat(self):
        if self.head==None: 
            return None
        else: 
            current=self.head
            if self.head.animal=="cat":
                store=self.head
                self.head=self.head.next
                return store
            while(current.next!=None):
                if current.next.animal=="cat":
                    store=current.next
                    current.next=current.next.next
                    return store
                else: 
                    current=current.next
            
            if current==None: 
                return None
    
    def dequeueDog(self):
        if self.head==None: 
            return None
        else: 
            current=self.head
            if self.head.animal=="dog":
                store=self.head
                self.head=self.head.next
                return store
            while(current.next!=None):
                if current.next.animal=="dog":
                    store=current.next
                    current.next=current.next.next
                    return store
                else: 
                    current=current.next
        
            if current==None: 
                return None
    def print(self):
        par=self.head
        while(par!=None):
            print(str(par.time)+"-"+str(par.animal)+" ->",end="")
            par=par.next
        print()

def main(): 
    st=Queue()
    st.enqueue(1,"cat")
    st.enqueue(9,"dog")
    st.enqueue(5,"cat")
    st.enqueue(7,"dog")
    st.enqueue(4,"cat")
    print("head age is "+str(st.head.time)+" head animal is "+str(st.head.animal))
    print("tail age is "+str(st.tail.time)+" tail animal is "+str(st.tail.animal))
    st.print()
    st.dequeueAny()
    st.print()
    print("dequeue cat: ")
    st.dequeueCat()
    st.print()
    print("dewequeue dog: ")
    st.dequeueDog()
    st.print()

if __name__ == "__main__":
     main()
        

