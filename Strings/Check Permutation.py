
from sys import stdin


def isPermutation(string1, string2) :
    if(sorted(list(string1)) == sorted(list(string2))):
        return True
    return False
    
#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

