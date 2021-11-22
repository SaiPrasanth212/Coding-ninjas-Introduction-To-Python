N = int(input())
Sum_of_Even_Digits = 0
Sum_of_Odd_Digits = 0

while (N > 0):
    remainder = N % 10
    if remainder%2 == 0:
        Sum_of_Even_Digits = Sum_of_Even_Digits + remainder
    else:
        Sum_of_Odd_Digits = Sum_of_Odd_Digits + remainder
    N = N // 10
    
print(Sum_of_Even_Digits , Sum_of_Odd_Digits)
