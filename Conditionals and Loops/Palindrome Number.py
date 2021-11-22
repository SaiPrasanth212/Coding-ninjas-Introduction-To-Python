n = int(input())
rev = 0
temp =n
while temp > 0:
    a = temp % 10
    rev = rev * 10 + a
    temp = temp // 10

if(n == rev):
    print("true")
else:
    print("false")
