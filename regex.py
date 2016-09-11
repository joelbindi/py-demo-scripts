import re 

#New way
fhand = open('regex_sum_221097.txt')
count = []
x = 0
newx = 0
for line in fhand: 
	if re.findall('[0-9]', line):
		line.split()
		stringList = re.findall('[0-9]+', line)
		count = [int(x) for x in stringList]
		for x in count:
			newx = newx + x
print newx

# for line in fhand: 
# 	if line.find('From: ') >= 0 :
# 		print line

#using Regex
# fhand = open('mbox-short.txt')

# x = 'my fave numbres are 4,5 and 8'
# y = re.findall('[0-9]+',x)
# print y

# x = 'From: Using the : character'
# y = re.findall('\$', x)
# print y