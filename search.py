import re 

#Old way
fhand = open('mbox-short.txt')

for line in fhand: 
	if line.find('From: ') >= 0 :
		print line

#using Regex
# fhand = open('mbox-short.txt')

for line in fhand: 
	line = line.strip()
<<<<<<< HEAD
	if re.search('^X-', line) >= 0:
		print line

x = 'my fave numbres are 4,5 and 8'
y = re.findall('[0-9]+',x)
print y

x = 'From: Using the : character'
y = re.findall('\$', x)
print y
=======
	if re.findall('From: ', line) >= 0:
		print line
>>>>>>> 8045e4c3f9bacfd3fc00a7fc477eb7c418389bdd
