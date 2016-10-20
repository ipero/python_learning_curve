# slice strings and lists
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  =   animals[3:6]            # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end
print cat, dog, frog

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]        # The last two items (index four and five)
print middle
print last


# find index of string in a list, then add new string into list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"
animals.insert(duck_index, "cobra")
print animals

# for in Python is different from JavaScript
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list: # number gets assigned value of each list item
    square_list.append(number**2)

square_list.sort()
print square_list

# store checkout shopping list
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] -=1
    return total
print "Your total grocery bill is $%s" % compute_bill(shopping_list)

#-------------------------------------------------------------------------------
# more practice with list and dictionary
# find a class average score and grade
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

all_students = [lloyd, alice, tyler]

def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    score = homework * .1 + quizzes * .3 + tests * .6
    return score

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
get_letter_grade(get_average(lloyd))

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

class_average = get_class_average(all_students)
print "A class average score is %s percent" % (class_average)

print "A class average grade is %s " % get_letter_grade(class_average)

#-------------------------------------------------------------------------------

# difference between .pop(), .remove() and del()
#n.pop(index) will remove the item at index from the list and return it to you
n = [ 3, 0, 6, 9, 14, 8, 20]
x = n.pop(4)
print x
print n

#n.remove(item) will remove the actual item if it finds it:
n = [ 3, 0, 6, 9, 14, 8, 20]
n.remove(6) # 4emoves 6 from the list, NOT the item at index 6
print n

#del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:
n = [ 3, 0, 6, 9, 14, 8, 20]
del(n[6])
print n

#-------------------------------------------------------------------------------

#The range function has three different versions:
# range(stop)
# range(start, stop)
# range(start, stop, step)
print range(4) # prints [0, 1, 2, 3]
print range(5, 10) # prints [5, 6, 7, 8, 9, 10]
print range(0,20, 2) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#-------------------------------------------------------------------------------
# difference between "for item in list" and "for i in range(len(list))"
n = [3, 5, 7]
# Method 1 is useful to loop through the list, but it's not possible to modify
# the list this way. Method 2 uses indexes to loop through the list, making it
#possible to also modify the list if needed.

# Method 1
def double_method_1(n):
    for item in n:
        item = item * 2
    return n
print double_method_1(n) # prints: [3, 5, 7] As you can see the list is same

# Method 2
def double_method_2(n):
    for i in range(0, len(n)):
        n[i] *= 2
    return n
double_method_2(n)
print n # prints: [6, 10, 14] It shows the list did change.

# The above two methods show when to use "for item in list" and when "for i in range"
