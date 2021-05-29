def isUnique(string1):
    occur={}
    for c in string1:
        occur[c]=0
    for c in string1:
        occur[c]+=1
        if occur[c]>1:
            return False
    
    return True

def isPermutation(str1,str2):
    if (len(str1)!=len(str2)):
        return False
    else: 
        for c in str1:
            if c not in str2:
                return False
        return True
        
def urlify(str1,length):
    if (length!=len(str1)):
        str1=str1.strip()
    result=""
    for c in str1:
        if c.isspace():
            result+="%20"
        else: 
            result+=c
    return result

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

    print(urlify("Mr John Smith   ",13))

if __name__ == "__main__":
    main()
