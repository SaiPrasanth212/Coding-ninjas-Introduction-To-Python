## Read input as specified in the question.
## Print output as specified in the question.

o = int(input())

while o != 6:
  
	if o <= 5 and o >= 1:

	    a = int(input())

	    b = int(input())
    
	if o == 1:
      
		print(a + b)
    
	if o == 2:
      
		print(a - b)
    
	if o == 3:
      
		print(a * b)
    
	if o == 4:
      
		print(a // b)
    
	if o == 5:
      
		print(a % b)  
  
	elif o < 1 or o > 6:
    
		print("Invalid Operation")
  
	o = int(input())
