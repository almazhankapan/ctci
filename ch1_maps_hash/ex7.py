def rotate_matrix(arr):
    '''
    1111
    2221
    3333
    4444

    4321
    4321
    4321
    4321

    i=0
    arr[i][i]-->arr[i][len-1-i]
    arr[i][i+1]-->arr[i+1][len-1-i]
    arr[i][i+2]-->arr[i+2][len-1-i]
    arr[i][i+3]-->arr[i+3][len-1-i]

    i=1
    arr[i+1][i]-->arr[i][len-1-(i+1)]
    arr[i+1][i+1]-->arr[i+1][len-1-(i+1)]
    arr[i+1][i+2]]-->arr[i+1][len-1-(i+1)]


    '''
    newarr=[]
    #try to think about optimizing it further
    for i in range(len(arr)):
        newarr.append([])
        for y in range(len(arr)):
            newarr[i].append(0)
    
    i=0
    last=len(arr)-1

    for i in range(len(arr)):
        for y in range(len(arr[i])):
            newarr[y][last-i]=arr[i][y]
    
    return newarr

def main():
    arr=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
    print(rotate_matrix(arr))

if __name__=="__main__":
    main()
            
