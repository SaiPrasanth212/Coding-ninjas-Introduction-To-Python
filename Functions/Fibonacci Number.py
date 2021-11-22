
def checkMember(n):
    a = 1
    b = 1
    c = 0
    if n == 0 or n == 1:
        print("true")
    else:
        while c < n:
            c = a + b
            b = a
            a = c
    if c == n:
        print("true")
    else:
        print("false")
    

n=int(input())
checkMember(n)
