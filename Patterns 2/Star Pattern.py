## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for r in range(n):
    s = n - r - 1
    char = 2 * r + 1
    #printing spaces
    for i in range(s):
        print(' ', end='')
    #printing symbols
    for j in range(char):
        print('*', end='')
    print()
