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
