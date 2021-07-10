def isPermutation(str1,str2):
    map1={}
    map2={}
    if len(str1)!=len(str2):
        return False
    str1="".join(sorted(str1))
    str2="".join(sorted(str2))
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
 
    return True

def main():
    string="almazhan"
    string2="nazhalma"
    #string="alma"
    #string2="nala"
    if isPermutation(string, string2):
        print(string+ " and "+string2+" are permutations")
    else: 
        print(string+ " and "+string2+" are not permutations")

if __name__=="__main__":
    main()
    

    