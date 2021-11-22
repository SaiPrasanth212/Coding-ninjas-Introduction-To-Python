## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

increasing = (n + 1)//2
decreasing = n - increasing

i = 1
while i <= increasing:

    # printing spaces 1st row has 0 spaces, 2nd row has 1 so ith will have i - 1 spaces
    s = 1
    while s <= i - 1:
        print(" ", end="")
        s = s + 1

    # printing stars 1st row has 1 star, 2nd row has 2 so ith will have i stars
    j = 1
    while j <= i:
        print("* ", end="")
        j = j + 1
    print()
    i = i + 1

i = 1
while i <= decreasing:
    # printing spaces 1st row has 2 spaces, 2nd row has 1 so ith will have decreasing - i spaces
    s = 1
    while s <= decreasing - i:
        print(" ", end="")
        s = s + 1

    # printing stars 1st row has 3 star, 2nd row has 2 so ith will have decreasing - i + 1 stars
    j = 1
    while j <= decreasing - i + 1:
        print("* ", end="")
        j = j + 1
    print()
    i = i + 1
