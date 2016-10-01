# squares = [i**2 for i in range(1,11)]

# print filter(lambda x: x >= 30 and x <= 70, squares)

# mylist = range(1,16)

# threes_and_fives = filter(lambda x: x % 5 == 0 or x % 3 == 0, mylist)

# print threes_and_fives


# garbled = '!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI'
# message = garbled[::-2]

garbled = 'IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX'
message = filter(lambda x: x != 'X', garbled)
print message