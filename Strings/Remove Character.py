
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
    op = ''
    for i in string:
        if i != ch:
            op = op + i
    return op

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
