## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for r in range(n):
    s = n - r - 1
    #printing spaces
    for i in range(s):
        print(' ', end='')
    #printing increasing
    for j in range(r+1, 2*r+2):
        print(j, end='')
    #printing decreasing
    for k in range(2*r, r,-1):
        print(k, end = '')
    print()
    
