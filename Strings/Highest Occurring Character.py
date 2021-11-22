
from sys import stdin


def highestOccuringChar(string) :
	#Your code goes here
    d = {}
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
            
    ans = 0
    maximum = 0
            
    for j,k in d.items():
        if k > maximum:
            ans = j
            maximum = k
    return ans

#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
