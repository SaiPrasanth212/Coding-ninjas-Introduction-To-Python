def alphabet(N):
    num = 65
    for i in range(0, N):
        for j in range (0, i + 1):
            ch = chr(num)
            print(ch, end = '')
        num = num + 1
        print()

N = int(input())
alphabet(N)
