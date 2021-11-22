'''
    Time Complexity : O(N * M)
    Space Complexity : O(max(N,M))

    Where N is the number of rows in the matrix,
          M is the number of columns in the matrix.
'''



import sys
from sys import stdin


def spiralPathHelper(matrix, r, c, rows, cols, ans):
    
    
    #If outside the matrix
    if (r >= rows or c >= cols):
        return
    
    #Push First Row
    for p in range(c, cols):
        
        ans.append(matrix[r][p])
        
    
    #Push Last Column
    for p in range(r + 1, rows):
        ans.append(matrix[p][cols - 1])

        
    #Push Last Row, if Last and First Row are not same
    if((rows - 1) != r):
        
        for p in range(cols - 2, c - 1, -1):
            ans.append(matrix[rows - 1][p])
            
            
    #Print First Column,if Last and First Column are not same
    if ((cols - 1) != c):
        
        for p in range(rows - 2, r, -1):
            ans.append(matrix[p][c])
            
            
    #Make recursive call on smaller submatrix
    spiralPathHelper(matrix, r + 1, c + 1, rows - 1, cols - 1 ,ans)
    


def spiralPathMatrix(matrix, n, m):
    
    r = 0
    c = 0
    
    ans = []
    
    #Take help of helper function to pass recursive calls
    spiralPathHelper(matrix, r, c, n, m, ans)
    
    return ans




t = int(input().strip())

for j in range(t):
    
    n,m = list(map(int, stdin.readline().strip().split(" ")))
    
    arr = []
    
    for i in range(n):
        
        a = list(map(int, stdin.readline().strip().split(" ")))
        arr.append(a)
            
    
    for i in spiralPathMatrix(arr, n, m):
        print(i, end = " ")
        
    print()
    
    

