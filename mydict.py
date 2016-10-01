# my_dict = {
# 	"Name": "Joel",
# 	"Age": 30,
# 	"BDFL": True
# }

# # print my_dict.keys()
# # print my_dict.values()

# for key in my_dict:
# 	print key, " ", my_dict[key]


# doubles_by_3 = [x**2 for x in range(1,6) if (x**2) % 3 == 0]
# even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

# print doubles_by_3


# print even_squares

# cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]

# print cubes_by_four

# l = [i ** 2 for i in range(1,11)]

# print l[2:9:2]


# my_list = range(1,11)

# print my_list[::2]

# to_21 = range(1,22)

# odds = to_21[::2]

# print odds
# middle_third = to_21[7:14]
# print middle_third

# languages = ["HTML", "Javascript", "Python","Ruby"]

# print filter(lambda x: x == "Python", languages)

one_to_ten = range(1,10)
count = 0
for x in one_to_ten:
	squared = x ** 2
	one_to_ten.append(squared)
	count = count + 1
	print 'Count', count

print one_to_ten
