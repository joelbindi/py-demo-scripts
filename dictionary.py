#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"

fname = "mbox-short.txt"
fh = open(fname)
# text = handle.read()
# words = text.split()

for line in fh:
	if "From " in line:
		words = line.split()
		words = words[1]
		print words

cou = dict()
for wrd in words:
	cou[wrd] = cou.get(wrd,0) + 1
print cou