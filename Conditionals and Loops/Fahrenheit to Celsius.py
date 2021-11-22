# Read input as sepcified in the question
# Print output as specified in the question

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
##      print(val1, " ", val2)


s = int(input())
e = int(input())
w = int(input())
while True:
    c = 0
    if s <= e:
        c = (s - 32)*5/9
        print(s , int(c))
        s = s + w
    else:
        break

