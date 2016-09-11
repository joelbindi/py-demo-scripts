# import urllib
import xml.etree.ElementTree as ET

tree = ET.parse('comments_221099.xml')
root = tree.getroot()

total = 0
count = 0

for x in root.findall('./comments/comment/count'):
	xint = int(x.text)
	count = count + xint
	total = total + 1

print 'Count', total
print 'Sum', count