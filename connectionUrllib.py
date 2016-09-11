import urllib

fhand = urllib.urlopen('http://www.py4inf.com/page1.html')

counts = dict()
for line in fhand:
	words = line.strip()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print counts