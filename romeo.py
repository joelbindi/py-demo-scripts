#fname = raw_input("Enter file name: ")
# fh = open(fname)
fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
	words = line.split()
	words.sort()
	x = 0
	if words not in lst:
		lst.append(words[0])
		lst.append(words[1])
		lst.append(words[2])
		lst.append(words[3])
		lst.append(words[4])
		lst.append(words[5])
		lst.append(words[6])
		lst.append(words[7])
	
lst.sort()
myList = sorted(set(lst))
print myList


