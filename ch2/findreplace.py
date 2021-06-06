def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    table={}
    index=0
    string="abcdefghijklmopqrstu"
    out=""
    seen={}
    for ch in pattern:
        if ch not in seen:
            seen[ch]=string[index]
            ch=string[index]
            out+=ch
            index+=1
        else:
            ch=seen[ch]
            out+=ch
            index+=1
    print(out)
    seenW={}
    index=0
    outW=""
    result=[]
    for w in words:
        for ch in w:
            if ch not in seenW:
                seenW[ch]=string[index]
                ch=string[index]
                outW+=ch
                index+=1
            else:
                ch=seenW[ch]
                outW+=ch
                index+=1
        if outW==out:
            result.append(w)
        print(outW)
        outW=""
        index=0
        seenW={}
            
    return result

def main():
    out=findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb")
    print(out)

if __name__ == "__main__":
    main()
            