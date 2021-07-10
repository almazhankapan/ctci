class LinkedList: 
    class Node: 
        def __init__(self, value, next):
            self.value=value
            self.next=None
    
    def __init__(self):
        self.head=None
        self.length=0
    
    def push(self, value):
        n=self.Node(value, None)
        if self.head==None: 
            self.head=n
        else: 
            h=self.head
            while(h.next!=None):
                h=h.next
            h.next=n
        self.length+=1

    
    def delete(self, value):
        found=False
        h=self.head
        if h.value==value: 
            self.head=self.head.next
        else: 
            while(h.next!=None):
                if h.next.value==value: 
                    h.next=h.next.next
                    found=True
                    return value
            if found==False: 
                return None
        self.length-=1

    def print(self):
        h=self.head
        while(h!=None):
            print(str(h.value)+"->",end="" )
            h=h.next
        print()
    
    def kthToLast(self, k):
        h1=self.head
        h2=self.head
        index=0   

        while(index!=k):
            h1=h1.next 
            index+=1    

        while(h1!=None):
            h1=h1.next 
            h2=h2.next 
        return h2
    
    def deleteMidNode(self):
        l=0
        h2=self.head
        while(h2!=None):
            l+=1
            h2=h2.next

        mid=int(l/2)
        h=self.head
        index=0
        while(index!=(mid-1)):
            h=h.next
            index+=1
        h.next=h.next.next

    def palindr(self):
        values=[]
        h=self.head
        if self.head.next==None: 
            return True
        l=0
        while(h!=None):
            l+=1
            values.append(h.value)
            h=h.next
        mid=l/2
        i=0
        while(i!=mid):
            if values[i]==values[l-(i+1)]:
                i+=1
            else: 
                return False
        return True
    
    def findLoop(self):
        h1=self.head
        h2=self.head.next
        while(h1!=None and h2!=None and h2.next!=None):
            if h1==h2:
                return h1
            h1=h1.next
            h2=h2.next.next
        return None
    
    def reverse(self):
        current=self.head
        prev=None
        while(current!=None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev


    

def intersect(l1,l2):
    len1=len2=0
    h1=l1.head
    h2=l2.head
    while(h1!=None):
        len1+=1
        h1=h1.next
    
    while(h2!=None):
        len2+=1
        h2=h2.next
    
    diff=len1-len2
    if diff>0:
        while(diff!=0):
            h1=h1.next
            diff-=1
    elif diff<0:
        diff=diff*(-1)
        while(diff!=0):
            h2=h2.next
            diff-=1
    
    while(h1!=None):
        if h1==h2:
            return h1
        else: 
            h1=h1.next
            h2=h2.next

        
#works for all
def removeDup(head):
    h=head
    map1={}
    l=LinkedList()
    h2=l.head
    while(h!=None):    
        if h.value in map1:
            h=h.next
        else: 
            l.push(h.value)
            map1[h.value]=1
            h=h.next
    head.value=l.head.value
    head.next=l.head.next

def partition(head, v):
    larger=LinkedList()
    smaller=LinkedList()
    h=head
    
    while(h!=None):
        if h.value<v:
            smaller.push(h.value)
            h=h.next
        else: 
            larger.push(h.value)
            h=h.next
    
    sh=smaller.head
    while(sh.next!=None):
        sh=sh.next
    sh.next=larger.head
    
    head.value=smaller.head.value
    head.next=smaller.head.next

def sumLists(l1,l2):
    l1=l1.head
    l2=l2.head
    sumL=LinkedList()
    carry=0
    while(l1!=None):
        s=l1.value+l2.value
        if carry==1:
            s+=1
        sumL.push(s%10)
        if(s>=10):
            carry=1
        else: 
            carry=0
        l1=l1.next
        l2=l2.next
    if carry==1:
        sumL.push(1)
    return sumL


'''
def sumListsF(l1,l2):
    l1=l1.head
    l2=l2.head
    sumL=LinkedList()
    carry=0
    while(l1!=None):
        s=l1.value+l2.value
        if carry==1:
            s+=1
        sumL.push(s%10)
        if(s>=10):
            carry=1
        else: 
            carry=0
        l1=l1.next
        l2=l2.next
    if carry==1:
        sumL.push(1)
    return sumL
'''


    
def main():
    l=LinkedList()
    l.push(3)
    l.push(4)
    l.push(5)
    l.delete(4)
    l.push(5)
    l.push(5)
    l.push(6)
    l.push(8)
    l.push(4)
    l.push(6)
    l.print()
    removeDup(l.head)
    l.print()
    l.push(11)
    l.push(7)
    l.print()
    print((l.kthToLast(5)).value)
    l.deleteMidNode()
    l.print()
    partition(l.head, 6)
    l.print()
    l1=LinkedList()
    l1.push(7)
    l1.push(1)
    l1.push(6)
    l2=LinkedList()
    l2.push(5)
    l2.push(9)
    l2.push(2)
    (sumLists(l1,l2)).print()
    lpal=LinkedList()
    lpal.push(1)
    lpal.push(2)
    lpal.push(4)
    lpal.push(3)
    lpal.push(2)
    lpal.push(1)
    if (lpal.palindr()):
        print("is palind")
    else: 
        print("not palind")
    lpal.print()
    lpal.reverse()
    lpal.print()


if __name__=="__main__": 
    main()
    
            
                
            




