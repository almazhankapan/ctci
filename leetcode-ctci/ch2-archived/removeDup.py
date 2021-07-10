# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        map1={}
        copy=ListNode(head.val, None)
        h=copy
        map1[head.val]=1
        head=head.next
        while(head!=None):
            if head.val not in map1:
                map1[head.val]=1
                newN=ListNode(head.val, None)
                copy.next=newN
                copy=copy.next
                head=head.next
            else:
                head=head.next
                
                
                
        
        return h

def main():
    w=ListNode(3,None)
    g=ListNode(3,w)
    s=ListNode(2,g)
    m=ListNode(1,s)
    l=ListNode(1,m)
    node=l
    while(node!=None):
        print(node.val, end="=>")
        node=node.next
    print()
    newL=deleteDuplicates(l)
    node=newL
    while(node!=None):
        print(node.val, end="=>")
        node=node.next
    print()

if __name__ == "__main__":
    main()
    
    
