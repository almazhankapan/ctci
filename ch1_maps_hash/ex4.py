def isPalindromePerm(string1):
    string2=""
    for ch in string1:
        if ch!=" ":
            string2+=ch
    string2=string2.lower()
    map1={}
    for ch in string2:
        if ch in map1:
            map1[ch]+=1
        else: 
            map1[ch]=1
    ones=0
    for ch in map1:
        if map1[ch]==1:
            ones+=1
            if ones>1:
                return False
        elif map1[ch]%2!=0:
            return False
    return True

def main():
    string="Tact Coa"
    print(isPalindromePerm(string))
    string="Tact eCoa"
    print(isPalindromePerm(string))
    

if __name__=="__main__":
    main()