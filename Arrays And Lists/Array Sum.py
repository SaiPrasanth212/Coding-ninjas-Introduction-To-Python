## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
li = []
sum = 0
li = [int(x) for x in input().split()]
for ele in li:
    sum = sum + ele
print(sum)
