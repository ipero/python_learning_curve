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

# Your code here!
animals.insert(duck_index, "cobra")


print animals
