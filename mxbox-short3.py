#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"

fh = open(fname)

for line in fh:
	if "From " in line:
		words = line.split()
		words = words[1]
		print words



# stuff = dict()
