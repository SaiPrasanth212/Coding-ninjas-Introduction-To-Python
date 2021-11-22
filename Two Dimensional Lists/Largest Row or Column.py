'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    maxrow=-2147483648
    maxcol=-2147483648
    maxindex=0
    max_index=0
    for i in range(nRows):
        sum=0
        for j in range(mCols):
            sum+=mat[i][j]
        if sum>maxrow:
            maxrow=sum
            maxindex=i
    for j in range(mCols):
        sum=0
        for ele in mat:
            sum+=ele[j]
        if sum>maxcol:
            maxcol=sum
            max_index=j
    if maxrow>=maxcol:
        print("row",maxindex,maxrow)
    else:
        print("column",max_index,maxcol)
    
#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
