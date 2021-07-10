def stringRotate(string1,string2):
    newString=string2+string2
    if string1 in newString: 
        return True
    else: 
        return False

def main():
    print(stringRotate("waterbottle","erbottlewat"))
    print(stringRotate("waterbottle","erbottle"))

if __name__=="__main__":
    main()