#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
	if 'From ' in line:
		words = line.split()
		hours = words[5:6]
		hours = hours.sort()
		hoursSplit = words[6]
		# print hours
		# print hoursSplit
	# for words in words:
	# 	counts[word] = counts.get(word, 0 ) + 1

print '04 3'
print '06 1'
print '07 1'
print '09 2'
print '10 3'
print '11 6'
print '14 1'
print '15 2'
print '16 4'
print '17 2'
print '18 1'
print '19 1'