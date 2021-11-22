


def printTable(start,end,step):
    while True:
        c = 0
        if start <= end:
            c = (start - 32)*5/9
            print(start, int(c))
            start = start + step
        else:
            break
	

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





