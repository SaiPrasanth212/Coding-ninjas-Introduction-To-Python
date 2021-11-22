## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
    	print('*', end = '')
    	j = j + 1
    i = i + 1
    print()
