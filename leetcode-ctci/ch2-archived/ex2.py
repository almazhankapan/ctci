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
        print()

def removeDuplicates(list):
    node=list.head
    buffer=[]
    if node==None: 
        return
    else: 
        buffer.append(node.data)#113
        while (node!=None):
            if node.next.data in buffer: 
                node.next=node.next.next 
            node=node.next
            if node!= None: 
                buffer.append(node.data)
        
def checkDuplicate(data,  list):
    head=list.head
    if head!=None: 
        if head.data==data: 
            head=head.next
    while(head!=None):
        if head.next!=None and head.next.data==data: 
            head.next=head.next.next
        head=head.next



def removeDuplicatesNoBuf(list):
    head=list.head
    node=head
    if node==None: 
        return
    else: 
        while(node!=None):
            checkDuplicate(node.data, list)
            node=node.next

#removeDup--new from solutions--have a runner up node
def removeDup2(list):
    node=list.head
    while(node!=None):
        current=node
        while(current.next!=None):
            if current.next.data==node.data: 
                current.next=current.next.next
            else: 
                current=current.next
        node=node.next

                

def kthToLast(list, k): 
    h=list.head
    length=0
    while(h!=None): #O(n)
        h=h.next
        length+=1

    index=length-k
    h=list.head
    i=0
    while(i!=index): #O(n)
        h=h.next
        i+=1
    return h.data

#kth to last-recursive--from solution book
#aabbccd---0,1,2,3
def kthToLastNew(node, k): #note here:  we can pass node, not whole list
    if node==None: 
        return 0
    else: 
        index=kthToLastNew(node.next, k)+1
        if (index==k):
            print("kth element is "+str(node.data))  #can't return node.data --- just print it
            #since need to return index for recursive a
        return index


#has access only to that node--not head    
def deleteMiddleNotCorrect(list):
    h=list.head
    length=0
    while(h!=None): #O(n)
        h=h.next
        length+=1
    index=0
    
    index=int(length/2)
    
    h=list.head
    i=0
    while(i!=index-1): #O(n)
        h=h.next
        i+=1
    h.next=h.next.next

#Note! delete node in the middle
#just reassignment - aka node=node.next does not work
#need to do node.data=node.next.data etc
def deleteMiddle(node):
    if node==None: 
        return False
    else: 
        node.data=node.next.data
        node.next=node.next.next
        return True

def findMiddle(list):
    l=0
    head=list.head
    node=head
    while (node!=None):
        l+=1
        node=node.next
    
    index=int(l/2)
    i=0
    h=head
    while(i!=index):
        h=h.next
        i+=1

    return h


#incorrect--returns string-should return linked list
def sumListsFor(list1,list2):
    h1=list1.head
    h2=list2.head
    num1=num2=""
    while(h1!=None):
        num1+=str(h1.data)
        h1=h1.next

    while(h2!=None):
        num2+=str(h2.data)
        h2=h2.next
    
    num1=int(num1)
    num2=int(num2)
    sum=num1+num2
    return sum

#implementing like solution
def sumListsFor2(l1,l2):
    h1=l1.head
    h2=l2.head
    sumList=LinkedList()
    sum1=0
    carry=0
    while (h1!=None):
        sum1=(h1.data+h2.data+carry)
        if sum1>10:
            carry=1
        else: 
            carry=0
        sumList.insert((sum1%10))
        h1=h1.next
        h2=h2.next
        if h1==None: 
            if carry>0:
                sumList.insert(1)
            

    return sumList    

def sumListsBack(list1,list2):
    h1=list1.head
    h2=list2.head
    num1=num2=""
    while(h1!=None):
        num1+=str(h1.data)
        h1=h1.next

    while(h2!=None):
        num2+=str(h2.data)
        h2=h2.next
    
    num1=int(''.join(reversed(num1)))
    num2=int(''.join(reversed(num2)))
    sum=num1+num2
    return sum

def sumListsBack2(h1,h2):
    #2 4 6
    #1 3 5
    #3 8 1
    sumList=LinkedList()
    if h1.next==None:
        sum=h1.data+h2.data
        if sum>10:
            carry=1
        else: 
            carry=0
        
        return carry
    else: 
        sum=sumListsBack2(h1.next, h1.next)
        sumList.insert((sum))
        return sum
        




    










def isPalindrome(list):
    str1=""
    node=list.head
    while(node!=None):
        str1+=str(node.data)
        node=node.next
    
    len1=len(str1)#1111111
    if len1%2==0:
        mid=int(len(str1)/2-1)
        second="".join(reversed(str1[mid:len1]))
    else: 
        mid=int(len(str1)/2)
        second="".join(reversed(str1[(mid+1):len1]))

    first=str1[0:mid]
    if first==second: 
        return True
    else: 
        return False

def reverseList(list1):
    prev=None
    current=list1.head
    while(current!=None):
        next=current.next
        current.next=prev
        if prev!=None: 
            current.next.data=prev.data
        prev=current #move one step
        if current!=None: 
            prev.data=current.data
        current=next
        if next!=None: 
            current.data=next.data #move one step 
    list1.head=prev
    if prev!=None: 
        list1.head.data=prev.data
    return list1



#new palindrome check

def isPalindrome2(listA):
    print("original")
    listA.print()
    listRev=reverseList(listA)
    print("reverse")
    print()
    listRev.print()
    #check if reverse is equal
    h1=listA.head
    h2=listRev.head
    while(h1!=None):
        if h1.data==h2.data: 
            h1=h1.next
            if h1!=None and h1.next!=None: 
                h1.data=h1.next.data
            h2=h2.next
            if h2!=None and h2.next!=None: 
                h2.data=h2.next.data
        else: 
            return False
    
    return True

#note--this one is incorrect--you should return not boolean
#but
def intersect(l1,l2):
    start1=l1.head
    start2=l2.head

    l1set=[]
    while(start1.next!=None):
        l1set.append(start1)
        start1=start1.next
        

    while(start2.next!=None):
        if start2 in l1set: 
            return start2
        else: 
            start2=start2.next
    
    #see if the last nodes intersect
    if start1!=start2:
        return None


def loopDetect(list):
    buffer=[]
    node=list.head
    while(node!=None):
        if node.data in buffer: 
            return True
        else: 
            buffer.append(node.data)
            node=node.next

    return False

def partition(list, p):
    h=list.head
    smaller=LinkedList()
    larger=LinkedList()
    while(h!=None):
        if h.data<p:
            smaller.insert(h.data)
            h=h.next
        else: 
            larger.insert(h.data)
            h=h.next
    
    s=smaller.head
    while(s.next!=None):
        s=s.next

    s.next=larger.head

    return smaller



def main(): 
    list=LinkedList()
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.delete(4)
    list.insert(5)
    list.insert(7)
    list.insert(9)
    list.insert(3)
    print("before removing duplicates: ")
    list.print()
    print("after removing duplicates: ")
    #removeDuplicates(list)
    removeDup2(list)#runner node and 2 while loops
    list.print()
    print()
    k=4
    print(str(k)+"th to last element is " + str(kthToLast(list, k)))
    kthToLastNew(list.head, k) #recursion-return index and print kth value
    print("before deleting middle: ")
    list.insert(2)
    list.insert(6)
    list.insert(8)
    list.print()
    print("after deleting middle: ")
    middle=findMiddle(list)
    #deleteMiddle(list)
    deleteMiddle(middle)
    list.print()
    print()
    listA=LinkedList()
    listA.insert(2)
    listA.insert(3)
    listA.insert(6)

    listB=LinkedList()
    listB.insert(1)
    listB.insert(3)
    listB.insert(5)
    print("list A")
    listA.print()
    print()
    print("list B")
    listB.print()
    print()
    #print(sumListsFor(listA, listB))
    print("sum-forward")
    sumFor=sumListsFor2(listA, listB)
    sumFor.print()
    print(sumListsBack(listA, listB))
    listPal=LinkedList()
    listPal.insert(1)
    listPal.insert(2)
    listPal.insert(3)
    listPal.insert(5)
    listPal.insert(3)
    listPal.insert(2)
    listPal.insert(1)
    listPal.insert(1)
    listPal.print()
    print()
    if isPalindrome2(listPal):
        print("is palindrome")
    else:
        print("not palindrome")
    
    if loopDetect(listPal):
        print("there's loop")
    else:
        print("there's no loop")
    print()
    partList=partition(listPal, 3)
    partList.print()
    


if __name__ == "__main__":
    main()