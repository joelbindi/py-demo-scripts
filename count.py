
count = []

# def count(sequence, item):
#     total = 0
#     for i in sequence:
#         if i == item:
#             total = total + 1
#     return total

# print count([1,2,1,1,1,3,3,3,3,3,3,3], 1)



def product(numbers):
	count = 1
	x = 1
	for x in numbers:
		count = x * count
	return count

print product([4, 5, 5])