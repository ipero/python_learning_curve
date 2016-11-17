import re

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

# r - raw string
# match - find match at the beginning of string
# search - search entire file
print(re.match(r'Ryan', data))
print(re.search(r'Chalkley', data))

def first_number(string):
    return re.search(r"\d", string)

def numbers(count, string):
    return re.search(r"\d"*count, string)
