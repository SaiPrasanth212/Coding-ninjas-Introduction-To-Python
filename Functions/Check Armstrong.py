## Read input as specified in the question.
## Print output as specified in the question.
def isArmstrong(n):
    l = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        dig = temp % 10
        sum += dig ** l
        temp = temp // 10
    if n == sum:
        print("true")
    else:
        print("false")


n = int(input())
isArmstrong(n)
