## Read input as specified in the question.
## Print output as specified in the question.
#main
n = int(input())

firstHalf = (n + 1) // 2
secondHalf = n // 2

#First Half
currRow = 1

while currRow <= firstHalf:
	spaces = 1
	while spaces <= (firstHalf - currRow) :
		print(" ", end = "")
		spaces += 1

	currCol = 1
	while currCol <= (2 * currRow) - 1 :
		print("*", end = "")
		currCol += 1

	print()
	currRow += 1

#Second Half
currRow = secondHalf

while currRow >= 1 :
	spaces = 1
	while spaces <= (secondHalf - currRow + 1) :
		print(" ", end = "")
		spaces += 1

	currCol = 1
	while currCol <= (2 * currRow) - 1 :
		print("*", end = "")
		currCol += 1

	print()
	currRow -= 1
