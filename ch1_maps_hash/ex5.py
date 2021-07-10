def insert(str1,str2):
    #len(str1)<str2
    i=j=0
    diff=0
    while(i!=len(str1)):
        if str1[i]==str2[j]:
            i+=1
            j+=1
        else: 
            if str1[i]==str2[j+1]:
                diff+=1
                if diff>1:
                    return False
                j+=1
            else: 
                return False
    if diff==1 and str1[len(str1)-1]==str2[len(str2)-1]:
        return True
    elif diff==0:
        return True
    else: 
        return False


        

def replace(str1,str2):
    
    i=0
    diff=0
    while(i!=len(str1)):
        if str1[i]==str2[i]:
            i+=1
        else: 
            diff+=1
            if diff>1:
                return False
            i+=1
    return True
            



def isOneAway(str1,str2):
    if len(str1)==len(str2):
        return replace(str1,str2)
    else: 
        diff=abs(len(str1)-len(str2))
        if diff!=1:
            return False
        else: 
            if len(str1)>len(str2):
                return insert(str2,str1)
            else: 
                return insert(str1,str2)

def main():
    print(isOneAway("pale","ple"))
    print(isOneAway("pales","pale"))
    print(isOneAway("pale","bale"))
    print(isOneAway("pale","bake"))
    print(isOneAway("pale","pke"))


    

if __name__=="__main__":
    main()