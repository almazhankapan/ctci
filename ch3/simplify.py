
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
        
    def print(self):
        while(not self.isEmpty()):
            print(self.pop(),end="")
        print()
    
    def retString(self):
        if self.isEmpty():
            return "/"
        out=[]
        while(not self.isEmpty()):
            out.append(self.pop())

        out= "".join(reversed(out))
        br=False
        if out[-1]=="/":
            br=True
        cur=len(out)-1
        while(br and cur>0):
            if out[cur]=="/":
                out=out[0:cur]
                cur-=1
            else: 
                break
        return out
            

            
def simplifyPath(path) :
        
    i=1
    st=Stack()
    st.push("/")
    st1=Stack()
    st1.push("/")
    temp=""
    arr=[]
    while(i!=len(path)):
        ch=path[i]
        if ch.isalpha():
            if i!=len(path)-1 and path[i+1]=="/":
                temp+=ch
                temp+=path[i+1]
                st1.push(ch)
                st1.push(path[i+1])
                st.push(temp)
                i+=2
                temp=""
            else:
                temp+=ch
                st1.push(ch)
                i+=1
        elif ch==".":
                if st1.peek()!="." and len(path)-2>i and path[i+1]=="." and path[i+2]=="/":
                    st.pop()
                    i+=1
                elif st1.peek()=="." and len(path)-1>i and path[i+1]!=".":
                    st.pop()
                    i+=1
                elif len(path)-1>i and path[i+1]=="/" :
                    i+=1
                else:
                    i+=1
                    st1.push(ch)
                    temp+=ch
                    if i==len(path):
                        st.push(temp)

        elif ch=="/": 
            if st1.peek()=="/":
                i+=1
            else:
                temp+=ch
                st.push(temp)
                st1.push(ch)
                i+=1

            

    
    #st.print()
    #st1.print()
    ret3=st.retString()
    print(ret3)

def simplify(path):
    st=Stack()
    st2=Stack()
    st.push(path[0])
    char=path[1]
    i=1
    temp=""
    while(i<len(path)):
        char=path[i]
        if(char!="/"):
            st.push(char)
            i+=1
            temp+=char
        elif(char=="/" and st.peek()=="/"):
            i+=1
        else: 
            st.push(char) 
            temp+=char
            i+=1
            if temp=="../" or temp=="..":
                st2.pop()
                temp=""
            elif temp=="./" or temp==".":
                temp=""
            else: 
                st2.push(temp)
                temp=""
    if temp==".." or temp=="../":
        st2.pop()
    else: 
        if not(temp=="./" or temp==".") and temp!="":
            st2.push(temp)
    
    if st2.isEmpty():
        st2.push("/")

    out=[]
    while(not st2.isEmpty()):
        out.append(st2.pop())
    
    out="".join(reversed(out))
    if out[0]!="/":
        out="/"+out
    if len(out)>1 and out[-1]=="/":
        out=out[0:-1]
        
    print(out)

    

        


                    
                         


def main(): 
    #removeOuterParentheses("(()())(())(()(()))")
    #removeOuterParentheses("(()())(())")
    #parenth("(()())(())(()(()))")
    simplify("/home///")
    simplify("/../")
    simplify("/a//b////c/d//././/..")
    #"/../"
    simplify("/home//foo/")
    simplify("/a/./b/../../c/")
    #"/a/./b/../../c/"


if __name__ == "__main__":
     main()
            
       
        