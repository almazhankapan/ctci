def compress(string):
    i=0
    curr_count=0
    final=""
    while(i!=len(string)):
        curr_count+=1
        if i<(len(string)-1):
            if string[i]==string[i+1]:
                i+=1
            else: 
                final+=(string[i]+str(curr_count))
                i+=1
                curr_count=0
                current=""
        else: 
            final+=(string[i]+str(curr_count))
            i+=1
    if len(string)<len(final):
        return string
    else: 
        return final

def main():
    string="aabcccccaa"
    print(compress(string))
    string="abc"
    print(compress(string))
        
if __name__=="__main__":
    main()