def longestPalindrome(s):
        res=[]
        maxLen=0
        maxString=""
        start=0
        end=0
        maxString+=s[0]
        maxLen=0
        i=0
        #for i in range(1,len(s)): #abcabc--a
        while(start!=len(s)-2):    
            end+=1
            substr=s[start:end]
            rev="".join(reversed(substr))
            if rev==substr:
                if len(substr)>maxLen:
                    maxString=substr
                    maxLen=len(substr)
            if end==len(s)-1:
                start+=1
                end=start+1
                
        
        
        return maxString

def main():
    out=longestPalindrome("babad")
    print(out)

if __name__ == "__main__":
    main()