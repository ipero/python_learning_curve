# zip will create pairs of elements when passed two lists, and will stop
# at the end of the shorter list.

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a,
    else:
        print b,
# prints: 3 9 17 15 30

# enumerate becomes very useful when do iteration over dictionary and you want
# to know how far you are in the iteration.
states = {
    "Minnesota": "MN",
    "North Dakota": "ND",
    "South Dakota": "SD",
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}
for index, state in enumerate(states):
    print index + 1, state
