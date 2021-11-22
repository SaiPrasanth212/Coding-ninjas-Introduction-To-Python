## Read input as specified in the question.
## Print output as specified in the question
N = int(input())
i = 1
while i <= N:
    j = 1
    start_chr = chr(ord('A') + N - i)
    while j <= i:
        charP = chr(ord(start_chr) + j - 1)
        print(charP, end = '')
        j = j + 1
    
    print()
    i = i + 1
