from sys import stdin 

def sort012(arr, n) :
    nextZero = 0
    nextTwo = (n - 1) 
    i = 0 
    while i <= nextTwo :
        if arr[i] == 0 :
            temp = arr[nextZero]
            arr[nextZero] = arr[i] 
            arr[i] = temp
            i += 1
            nextZero += 1
        elif arr[i] == 2 :
            temp = arr[nextTwo] 
            arr[nextTwo] = arr[i] 
            arr[i] = temp
            nextTwo -= 1
        else : 
            i += 1 


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1
