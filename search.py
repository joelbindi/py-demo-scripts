import re 

#Old way
# fhand = open('mbox-short.txt')

# for line in fhand: 
# 	if line.find('From: ') >= 0 :
# 		print line

#using Regex
fhand = open('mbox-short.txt')

for line in fhand: 
	line = line.strip()
	if re.findall('From: ', line) >= 0:
		print line