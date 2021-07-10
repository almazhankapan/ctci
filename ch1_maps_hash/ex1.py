def isUnique(string):
    map1={}
    for x in string: 
        if x in map1:
            map1[x]+=1
        else: 
            map1[x]=1
    
    for y in map1.values():
        if y!=1:
            return False
    
    return True


def main():
    string="assfsfbv"
    #string="almq"
    if isUnique(string):
        print(string+" is unique")
    else: 
        print(string+" is not unique")

if __name__=="__main__":
    main()