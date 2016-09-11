import json

data = '''

{
	"name" : "Chuck",
	"phone" : {
		"type" : "intl",
		"number" : "123424124"
	} ,
	"email" : {
		"hide" : "yes"
	}
}

'''

info = json.loads(data)
print 'Name', info['name']
print 'Phone & Email',info['email']['hide']

for item in info:
	print 'Name', info['name']
	print 'Phone & Email',info['email']['hide']