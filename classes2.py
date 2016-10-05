class Animal(object):
	"""Makes cute animals"""
	is_alive = True
	health = "good"
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def description(self):
		print self.name
		print self.age

hippo = Animal("Hipster","6")

hippo.description

sloth = Animal("jj","8")
ocelot = Animal("Geoge","9")

print hippo.health
print sloth.health
print ocelot.health

