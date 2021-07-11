
class Stack:
    class Node: 
        def __init__(self, data, next1):
            self.data=data
            self.next1=next1
        
    def __init__(self):
        self.size=0
        self.top=None
        
    def push(self,data):
        newN=self.Node(data, self.top)
        self.top=newN
        self.size+=1
        
    def pop(self):
        if self.top==None:
            return None
        else:
            data=self.top.data
            self.top=self.top.next1
            self.size-=1
            return data
        
    def peek(self):
        if self.top==None:
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.size==0
        
    def print1(self):
        while(not self.isEmpty()):
            print(self.pop(),end="")
        print()
            
def removeOuterParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    st1=Stack()
    '''
    for i in range(1,len(s)):
        char=s[i]
        if push==True: 
            st2.push(char)
            push=False
        if char==")" and st1.peek()=="(" and start==2:
            if s[i+1]==")":
                vn=st1.pop()
                vn2=st1.pop()
                st2.push(vn2)
                st2.push(vn)
                st2.push(char)
                push=True
        elif char==")" and st1.peek()=="(" and start==1:
            #print(char, end="")
            st2.push(char)
            var=st1.pop()
            #print(var, end="")
            st2.push(var)
            start-=1
        elif char==")" and st1.peek()=="(" and start==0:
            st1.pop()
            start-=1
        elif char =="(" :
            start+=1
            st1.push(char)
    st2.print1()
    '''    
    temp=""
    arr=[]
    for i in range(len(s)):
        char=s[i]
        if char=="(":
            st1.push(char)
        else: 
            st1.pop()
        
        temp+=char
        
        if st1.isEmpty():
            arr.append(temp) 
            temp=""

    print(arr)
        
        
def parenth(s):
    st=Stack()
    temp=""
    arr=[]
    for i in range(len(s)):
        char=s[i]
        temp+=char
        if char=="(":
            st.push(char)
        else: 
            st.pop()
        
        if st.isEmpty():
            arr.append(temp[1:-1])
            temp=""
    
    for s in arr: 
        print(str(s),end="")
            


def main(): 
    removeOuterParentheses("(()())(())(()(()))")
    #removeOuterParentheses("(()())(())")
    parenth("(()())(())(()(()))")

if __name__ == "__main__":
     main()
            
       
        