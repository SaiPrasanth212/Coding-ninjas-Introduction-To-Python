## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("1", end = "")
        j = j + 1
    i = i + 1
    print()
