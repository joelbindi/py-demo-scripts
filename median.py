def median(numbers):
	sequence=[]
	sequence=sorted(numbers)
	a=len(sequence)
	#float b 
	if a%2==0:
		# b=(sequence[a/2-1]+sequence[a/2-1+1])/2
		return (sequence[a/2-1]+sequence[a/2-1+1])*0.5
	else:
		return sequence[a/2-1+1]

print median([1,2,3,3,3,2,2,2,2,4,5,6,7,8,8,4])