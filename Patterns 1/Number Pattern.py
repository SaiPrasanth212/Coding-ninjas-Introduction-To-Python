## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())
for i in range(0,N):
    for j in range(1,N+1-i):
        print(j,end="")

    print() 
