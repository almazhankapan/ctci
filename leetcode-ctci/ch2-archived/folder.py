def getFolderNames(names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        out=[]
        new=""
        map1={}
        nextV={}

        for x in names: 
            map1[x]=0
            
        for x in names:
            if x not in out:
                out.append(x)
                if "(" in x:
                    ind=x.find("(")
                    num1=x[ind+1:ind+2]
                    str1=x[0:ind]
                    map1[x]+=1
                    if str1 in map1:
                        map1[str1]+=1
                    else: 
                        map1[str1]=1
                else: 
                    
                    map1[x]+=1
                
            else:
                if "(" in x and x in map1:
                    new=x+"("+str((map1[x]))+")"
                    map1[x]+=1
                    if new in map1:
                        map1[new]+=1
                    else: 
                        map1[new]=1
                    out.append(new)
                if "(" not in x and x in map1:
                    new=x+"("+str((map1[x]+1))+")"
                    map1[x]+=1
                    if new in map1:
                        map1[new]+=1
                    else: 
                        map1[new]=1
                    out.append(new)             
        return out
            


def main():
    out=getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"])
    # ["pes","fifa","gta","pes(2019)"]

    #["gta","gta(1)","gta","avalon"]
    #["wano","wano","wano","wano"]
    #["kaido","kaido(1)","kaido","kaido(1)"]
    #["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
    # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]

    print(out)

if __name__ == "__main__":
    main()
            