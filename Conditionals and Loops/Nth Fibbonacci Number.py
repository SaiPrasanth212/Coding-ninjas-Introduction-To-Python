## Read input as specified in the question.
## Print output as specified in the question.

''''def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)'''

def fibo(n):
    if n == 1 or n == 2:
        return 1
    x = 1
    y = 1
    while n > 2:
        z = x+y
        x = y
        y = z
        n = n-1
            
    return z
    
    
    
#main
n = int(input())
print(fibo(n))
