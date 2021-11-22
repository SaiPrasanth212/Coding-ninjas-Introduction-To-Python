import math

n = int(input())

for i in range(math.ceil(n/2)):

   for j in range(1,n+1):

       print(n*2*i + j ,end = " ");

   print()

for i in range(n//2,0,-1):

   for j in range(1,n+1):

       print(n*(2*i-1) + j , end = " ")

   print()
