# List Comprehension in Python
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print even_squares

cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
print cubes_by_four

# create a list of numbers where last digit of number has "5" in it
# use only list comprehension to solve it
fives = [x for x in range(1,1001) if x % 5 == 0 and x / 5 % 2 != 0]
print fives
# print out: [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145,
# 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305,
# 315, 325, 335, 345, 355, 365, 375, 385, 395, 405, 415, 425, 435, 445, 455, 465,
# 475, 485, 495, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 605, 615, 625,
# 635, 645, 655, 665, 675, 685, 695, 705, 715, 725, 735, 745, 755, 765, 775, 785,
# 795, 805, 815, 825, 835, 845, 855, 865, 875, 885, 895, 905, 915, 925, 935, 945,
# 955, 965, 975, 985, 995]
#-------------------------------------------------------------------------------
# list slicing
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]

# A negative stride progresses
my_list = range(1, 11)

backwards = my_list[::-1]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = [x for x in range(1,22)]
odds = to_21[::2]
middle_third = to_21[7:14]
print odds
print middle_third

# get secret message. It is revesed and we need every other letter
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message
#-------------------------------------------------------------------------------
# anonymous functions: lambda
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares) # prints [36, 49, 64]

# print secret message by filting out "X"
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
