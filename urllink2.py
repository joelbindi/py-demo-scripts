# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_221102.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
newx = 0
count = 0
tags = soup('span')
for tag in tags:
	tagC = tag.contents[0]
	tagInt = int(tagC)
	newx = newx + tagInt
	count = count + 1
print 'Sum ', newx
print 'Count ', count

