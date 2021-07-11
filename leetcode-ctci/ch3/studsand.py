
class Queue:
    def __init__(self):
        self.size=0
        self.arr=[]
    def enqueue(self,data):
        self.arr.append(data)
    def dequeue(self):
        if len(self.arr)>0:
            d=self.arr[0]
            lens=len(self.arr)
            self.arr=self.arr[1:lens]
            return d
    def isEmpty(self):
        return (len(self.arr)==0)
    def peek(self):
        return self.arr[0]
    def print(self):
        for x in self.arr: 
            print(x, end="")
        print()

def countStudents(students, sandwiches):
    i=0
    out=0
    start=0
    queueSa=Queue()
    queueSt=Queue()
    for i in range(len(sandwiches) ):
        queueSa.enqueue(sandwiches[i])
        queueSt.enqueue(students[i])
    
    
    i=0
    out=0
    sand=queueSa.dequeue()
    
    while(not queueSa.isEmpty()):
        if sand==queueSt.peek():
            queueSt.dequeue()
            sand=queueSa.dequeue()
        else: 
            if sand not in queueSt.arr:
                out=len(queueSt.arr)
                
                return out
            else:
                queueSt.enqueue(queueSt.dequeue())
    if sand==queueSt.dequeue():
        return 0
    else: 
        return 1
    
    
    
def main(): 
    students=[0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1]
    sandwiches=[1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]
    print(countStudents(students, sandwiches))
       
    #1
    #,0
    


if __name__ == "__main__":
     main()                
            
            
    
            
                
                
        #11001
        #00011
        
        #111
        #011