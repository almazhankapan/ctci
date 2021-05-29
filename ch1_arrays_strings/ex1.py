#ex 1.1
def isUnique(string1):
    occur={}
    for c in string1:
        occur[c]=0
    for c in string1:
        occur[c]+=1
        if occur[c]>1:
            return False
    else: 
        return True

#ex 1.2
def isPermutation2(str1,str2):
    if len(str1)!= len(str2):
        return False
    occur1=occur2={}
    for c in str1:
        occur1[c]=0
    
    for c in str1:
        occur1[c]+=1
        if c not in str2:
            return False
    #note that you don't need to iterate through second string
    #just substract number of occurences
    for c in str2:
        occur1[c]-=1
        if occur1[c]<0:
            return False
    
    
    return True

#1.2--effective solution--sort-strings-then-compare
def isPermutation(str1,str2):
    if len(str1)!= len(str2):
        return False

    sorted1 = sorted(str1)
    str1 = "".join(sorted1)

    sorted2 = sorted(str2)
    str2 = "".join(sorted2)
    
    if (str1!=str2):
        return False
    else: 
        return True



#1.3

def urlify1(string1, length):  
    replaced=""
    if len(string1)>length: 
        string1=string1.strip()
        print(len(string1))
    
    for c in string1:
        if c==' ':
            replaced+="%20"
        else: 
            replaced+=c
    
    return replaced

#1.3 another
#O(n) 
def urlify(string, length):
    string=string.strip()
    replace=""
    for i in range(len(string)): 
        if (not string[i].isspace()):
            replace+=string[i]
        if (string[i].isspace()):
            replace+="%20"
    diff=length-len(string)
    if (diff>0):
        add="%20" * diff
        replace+=add
    return replace

#1.4
def isPalindromePerm(string1):
    occur={}
    string1=(string1.strip()).lower()#O(1)
    #record only non-space characters
    for c in string1: #O(n)
        if not c.isspace():
            occur[c]=0
    #count number of occurences for non-space chars only 
    for c in string1: #O(n)
        if not c.isspace():
            occur[c]+=1
    ones=0
    for count in occur.values(): #O(n)
        if count %2 != 0:
            if count==1:
                ones+=1
                if ones>1:
                    return False
            else: 
                return False
    
    return True



#1.5--incorrect

def isOneEdit2(str1,str2):
    diff=0
    if(abs(len(str1)-len(str2))>1):
        return False
    else: 
        for c in str1:
            if c not in str2:
                diff+=1
                if (diff>1):
                    return False  
        return True

#1.5--modified

def isOneEdit(str1,str2):
    diff1=diff2=0
    if(abs(len(str1)-len(str2))>1):
        return False
    else: 
        for c in str1:
            if c not in str2:
                diff1+=1
                if (diff1>1):
                    return False 

        for c in str2:
            if c not in str1:
                diff2+=1
                if (diff2>1):
                    return False   
        
        return True

#1.6

def compress1(str1):
    replace=""
    occur={}
    for c in str1:
        occur[c]=[]

    index=-1
    for c in str1:
        index+=1
        #if this char appears first time
        if (len(occur[c])==0):
            occur[c].append(1)
            if ((index+1<len(str1) and str1[index]!=str1[index+1]) or (index+1==len(str1))):
                replace+=(c+"1")
        else: 
        #if it's not first time and previous char was the same
            if (index>0 and (str1[index]==str1[index-1])):
                occur[c][-1]+=1
                if ((index+1<len(str1) and str1[index]!=str1[index+1]) or (index+1==len(str1))):
                    replace+=(c+str(occur[c][-1]))
            else: 
                occur[c].append(1)
                if ((index+1<len(str1) and str1[index]!=str1[index+1]) or (index+1==len(str1))):
                    replace+=(c+str(occur[c][-1]))
    if len(str1)<len(replace):
        return str1
    else: 
        return replace

#1.6
def compress(string):
    hashTable={}
    for c in string: 
        hashTable[c]=[] 
    
    for i,c in enumerate(string): 
        if len(hashTable[c])==0:
            hashTable[c].append(1)
        else: 
            if string[i-1]==c:
                hashTable[c][-1]+=1
            else: 
                hashTable[c].append(1)
    

    
    if len(string)>len(compress):
        return compress
    else: 
        return string


        

#1.8
def zeroMatrix(matrix):
    #O(n^2)
    for i_row in range(len(matrix)): 
        for i_col in range(len(matrix[i_row])):
            if matrix[i_row][i_col]==0:
                targetRow=i_row
                targetColumn=i_col
                break
    #O(n^2--might not be always)
    for i_row in range(len(matrix)): 
        matrix[i_row][targetColumn]=0
        if i_row==targetRow: 
            for c in range(len(matrix[targetRow])):
                matrix[targetRow][c]=0

    for row in matrix: 
        print("[",end="")
        for c in row:
            print(c,end="")
        print("],")




def main():

    #ex 1.1
    if(isUnique("super")):
        print("unique")
    else: 
        print("not unique")
    
    #ex 1.2
    if (isPermutation("alma","mala")):
        print("is permutation")
    else:
        print("not permutation")

    #ex 1.3
    print(urlify("Mr John Smith      ",15))

    #ex 1.4
    if(isPalindromePerm("atco scat")):
        print("palindrome perm")
    else: 
        print("not palindrome perm")

    #ex 1.5

    if(isOneEdit("pale", "bale")):
        print("one edit")
    else: 
        print("not one edit")

    #ex 1.6
    print(compress("aabcccccaaa"))
    print(compress("aabcccccaaabbbbbbbb"))
    print(compress("acd"))

    #ex 1.8
    print(zeroMatrix([[1,2,4,5],[2,0,9,8],[2,3,4,8]]))

if __name__ == "__main__":
    main()
