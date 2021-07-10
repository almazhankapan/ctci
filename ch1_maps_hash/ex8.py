def zero_matrix(arr):
    '''
    1111
    2021
    3333
    4444

    1011
    0000
    3033
    4044


    '''
    row=-1
    column=-1
    for i in range(len(arr)):
        for y in range(len(arr[i])):
            if arr[i][y]==0:
                row=i
                column=y
                break
    if row!=-1:
        for i in range(len(arr)):
            for y in range(len(arr[i])):
                if i==row or y==column: 
                    arr[i][y]=0
    
    return arr


def main():
    arr=[[1,1,1,1],[2,0,2,2],[3,3,3,3],[4,4,4,4]]
    print(zero_matrix(arr))

if __name__=="__main__":
    main()                
            