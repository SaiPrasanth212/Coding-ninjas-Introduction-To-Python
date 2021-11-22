
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    '''arr = string.split(' ')
    op = []
    for i in arr:
        op.append(i[::-1])
    return " ".join(op)'''
    
    op = ''
    for i in string.split():
        op = op +' ' + i[::-1]
    return op[1:]

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
