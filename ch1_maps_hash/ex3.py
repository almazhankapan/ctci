def urlify(string, length):
    if length!=len(string):
        #great point for python
        string=string[0:length]
    out=""
    for ch in string: 
        if ch==" ":
            out+="%20"
        else: 
            out+=ch
    return out   

def main():
    string="Mr John Smith     "
    print(urlify(string, 13)+str("."))

if __name__=="__main__":
    main()