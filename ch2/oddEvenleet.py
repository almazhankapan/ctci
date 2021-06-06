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

def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head==None:
        return None
    if head.next==None:
        return head
    lEven=ListNode(0, None)
    lOdd=ListNode(head.val, None)
    sOdd=lOdd
    sEven=lEven
    index=1
    head=head.next
    firstE=True
    firstO=True
    while(head!=None):
        index+=1
        if index%2==0:
            if firstE==True:
                lEven.val=head.val
                print(lEven.val)
                head=head.next
                firstE=False
            else:
                newN=ListNode(head.val, None)
                lEven.next=newN
                lEven=lEven.next
                print(lEven.val)
                head=head.next
        else:
            if firstO==True:
                lOdd.val=head.val
                head=head.next
                print(lOdd.val)
                firstO=False
            else:
                newN=ListNode(head.val, None)
                lOdd.next=newN
                lOdd=lOdd.next
                head=head.next
            
        lOdd.next=sEven
        return sOdd


def main():
    w=ListNode(5,None)
    g=ListNode(4,w)
    s=ListNode(3,g)
    m=ListNode(2,s)
    l=ListNode(1,m)
    node=l
    node.print()

    newL=oddEvenList(node)
    newL.print()
    

if __name__ == "__main__":
    main()
