import urllib
from BeautifulSoup import *

# url = raw_input('Enter -', )

url = 'http://www.py4inf.com/'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
	print tag.get('href',None)

x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
type(x)