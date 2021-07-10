# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        while(self!=None):
            print(self.val, end="=>")
            self=self.next
        print()

def addTwoNumbers( l1, l2):
    if l1==None and l2==None:
        return None
    elif l1==None and l2!=None:
        return l2
    elif l2==None and l1!=None:
        return l1
    else: 
            
        sumL=ListNode(((l1.val+l2.val)%10),None)
        if (l1.val+l2.val)>=10:
            carry=1
        else:
            carry=0
        head=sumL
        l1=l1.next
        l2=l2.next
            
        while(l1!=None or l2!=None):
            if l1==None:
                newN=ListNode(((l2.val+carry)%10), None)
                sumL.next=newN
                sumL=sumL.next
                if (l2.val+carry)>=10:
                    carry=1
                else:
                    carry=0 
                l2=l2.next
            elif l2==None:
                newN=ListNode(((l1.val+carry)%10), None)
                sumL.next=newN
                sumL=sumL.next
                if (l1.val+carry)>=10:
                    carry=1
                else:
                    carry=0
                l1=l1.next
            else:
                newN=ListNode(((l1.val+l2.val+carry)%10), None)
                if (l1.val+l2.val+carry)>=10:
                    carry=1
                else:
                    carry=0
                sumL.next=newN
                sumL=sumL.next
                l1=l1.next
                l2=l2.next
        if carry==1:
            newN= ListNode(1, None)
            sumL.next=newN
        return head

def main():
    w=ListNode(9,None)
    g=ListNode(9,w)
    s=ListNode(9,g)
    m=ListNode(9,s)
    l=ListNode(9,m)
    d=ListNode(9,l)
    q=ListNode(9,d)
    node=q
    node.print()

    w1=ListNode(9,None)
    g1=ListNode(9,w1)
    s1=ListNode(9,g1)
    m1=ListNode(9,s1)
    node1=m1
    node1.print()
    newL=addTwoNumbers(node, node1)
    newL.print()
    

if __name__ == "__main__":
    main()

        
