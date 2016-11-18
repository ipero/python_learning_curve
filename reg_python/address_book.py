import re

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

# r - raw string
# match - find match at the beginning of string
# search - search entire file
print(re.match(r'Ryan', data))
print(re.search(r'Chalkley', data))

def phone_numbers(data):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)

# Find all phone numbers
def numbers(count, string):
    return re.search(r"\d"*count, string)

# Find all of the words in the string that are count word characters long or longer.
def find_words(count, string):
    return re.findall(r'\w{count}+', string)
