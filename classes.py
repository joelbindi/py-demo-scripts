class Fruit(object):
	"""A Class that makes various tasty fruits"""
	def __init__(self,name,color,flavor,poisonous):
		self.name = name
		self.color = color
		self.flavor = flavor
		self.poisonous = poisonous

	def description(self):
		print "I'm a %s %s and I taste like %s." % (self.color, self.name,self.flavor)

	def is_edible(self):
		if not self.poisonous:
			print "Yep! I'm edible."
		else: 
			print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon","yellow","sour", False)

lemon.description()
lemon.is_edible()

print '\n', '----------------', '\n'

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name 
        print self.age
        
hippo = Animal("Hipster", "6")

hippo.description()