## Read input as specified in the question.
## Print output as specified in the question.
lines=int(input())  
i=1  
j=1  
while i<=lines:  #this loop is used to print lines  
    j=1  
    while j<=lines:      #this loop is used to print lines  
        if i==j:  
            print("*", end='', flush=True)  
        else :  
            print("0", end='', flush=True)  
        j=j+1  
    j=j-1;  
    print("*", end='', flush=True)  
    while j>=1:  #this loop is used to print lines  
        if i==j:  
            print("*", end='', flush=True)  
        else :  
            print("0", end='', flush=True)  
        j=j-1  
    print("");  
    i=i+1  
