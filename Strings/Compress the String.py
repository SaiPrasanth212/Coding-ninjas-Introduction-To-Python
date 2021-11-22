
from sys import stdin


def getCompressedString(s) :
    c = 1
    op = s[0]
    for i in range(1, len(s)):
        if(s[i] == s[i-1]):
            c = c + 1
        else:
            if(c > 1):
                op = op + str(c)
            op = op + s[i]
            c = 1
    if c > 1:
        op = op + str(c)
    return op

#main
string = stdin.readline().strip();
ans = getCompressedString(string)

print(ans)
