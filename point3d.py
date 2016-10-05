class Point3D(object):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return ("(%d, %d, %d)") % (self.x,self.y,self.z) #check the spaces, there is one always

my_point = Point3D(1,2,3)
print my_point