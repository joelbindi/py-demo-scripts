#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

print "There were", count, "lines in the file with From as the first word"
