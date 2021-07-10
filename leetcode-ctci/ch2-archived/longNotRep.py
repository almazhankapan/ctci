'''
def lengthOfLongestSubstring( s):
    all_str=[]
    index1=0
    maxLen=0
    for i in range(len(s)): #abcabc--a
        curr=""
        index1=i
        for j in range(i,len(s)): #0
            ch=s[index1] #a
            if ch not in curr: 
                curr+=ch #a
                index1+=1
                if curr not in all_str: 
                    all_str.append(curr)
                    if maxLen<len(curr):
                        maxLen=len(curr)
            else: 
                break
    return maxLen
'''

def lengthOfLongestSubstring( s):
    mapS={}
    start=0
    end=0
    substr=""
    
    size=1
    mapS[s[0]]=0
    substr+=s[0]
    for i in range(1,len(s)):
        if s[i] not in substr: 
            end+=1
            mapS[s[i]]=i
            newS=end-start+1
            substr=s[start: end+1]
            size=max(size, newS)
        else: 
            end+=1

            start=mapS[s[i]]+1
            mapS[s[i]]=i
            newS=end-start+1
            size=max(size, newS)
            substr=s[start: end+1]
    print(size)
        
          
  
  
          


def main():
    out=lengthOfLongestSubstring("bbtablud")
    print(out)

if __name__ == "__main__":
    main()


