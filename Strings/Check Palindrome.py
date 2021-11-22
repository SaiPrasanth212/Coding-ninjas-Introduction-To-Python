
from sys import stdin


def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while(i < j):
        if string[i] != string[j]:
            return False
        i = i + 1
        j = j - 1
    return True   

#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

