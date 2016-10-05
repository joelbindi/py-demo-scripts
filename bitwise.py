
# print 5 >> 4  # Right shift
# print 5 << 1  # Left shift 
# print 8 & 5   # Bitwise AND
# print 9 | 4   # Bitwise OR 
# print 12 ^ 42 # Bitwise XOR
# print ~88     # Bitwise NOT

# print 0b1, #1
# print 0b10,#2
# print 0b11,#3
# print 0b100, #4
# print 0b101, #5
# print 0b110, #6
# print 0b111, #7
# print "******"
# print 0b1 + 0b11
# print 0b11 * 0b11



# myList = [2,3,4,5]
# for x in myList:
# 	print bin(x), '\n'

# print 0b1110 & 0b101

# x = 0b1110 ^ 0b101
# print bin(x)

# num = 0b1100
# mask = 0b0100
# desired = num & mask
# if desired > 0:
# 	print "Bit was on"

# def check_bit4(input):

# a = 0b11101110
# mask = 0b100
# desired = a ^ mask
# print bin(desired)

a = 0b101

#Tenth bit mask 
mask = (0b1 << 9) #one less than 10
desired = a ^ mask 
print desired

def flip_bit(number, n):
	a = number 
	mask = (n << 9)
	result = number ^ mask
	return result

print flip_bit(0b101,0b1)
