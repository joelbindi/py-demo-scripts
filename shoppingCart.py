# class ShoppingCart(object):
# 	"""Creates shopping cart objects
# 	for users of the website"""
# 	items_in_cart = {}
# 	def __init__(self,customer_name):
# 		self.customer_name = customer_name

# 	def add_item(self,product,price):
# 		"""Add product to cart"""
# 		if not product in self.items_in_cart:
# 			self.items_in_cart[product] = price
# 			print product + ' added.'
# 		else:
# 			print product + ' already in the cart'

# 	def remove_item(self,product):
# 		if product in self.items_in_cart:
# 			del self.items_in_cart[product]
# 			print product + ' removed.'
# 		else:
# 			print product + ' is not in cart'

# my_cart = ShoppingCart('Joel')
# my_cart.add_item('Milk',10)

# print my_cart.items_in_cart

class Customer(object):
	"""Produces objecst that represent customers"""
	def __init__(self,customer_id):
		self.customer_id = customer_id

	def display_cart(self):
		print "I'm a string that stands for the items in a cart"

class ReturningCustomer(Customer):
	"""For customers in a repeated variety"""
	def display_order_history(self):
		print "I'm a string that stands for your order history"

monty_python = ReturningCustomer("ID: 144")
monty_python = display_cart()
monty_python = display_order_history()

