## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 0
while i < n:
    s = n - i - 1
    num = n - s
    #printing spaces
    p = 0
    while p < s:
        print(' ', end='')
        p = p + 1
    #printing numbers
    q = 1
    while q <= num:
        print(q, end = '')
        q = q + 1
    print()
        
    i = i + 1
    
