
from sys import stdin

def removeConsecutiveDuplicates(string) :
    op = string[0]
    for i in range(1, len(string)):
        if(string[i] != string[i-1]):
            op = op + string[i]
    return op
        
#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
