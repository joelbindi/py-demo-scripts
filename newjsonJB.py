import json

total = 0
count = 0

with open('comments_221103.json') as data_file:    
    data = json.load(data_file)
    for x in data['comments']:
    	xint = int(x['count'])
    	count = count + xint
    	total = total + 1
print 'Sum', count
print 'Count', total
 
#urllib wont load