import re

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

# r - raw string
# match - find match at the beginning of string
# search - search entire file
print(re.match(r'Ryan', data))
print(re.search(r'Chalkley', data))

# Find all phone numbers
def phone_numbers(data):
    return re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)


def numbers(count, string):
    return re.search(r"\d"*count, string)

# Find all of the words in the string that are count word characters long or longer.
def find_words(count, string):
    return re.findall(r"\w{%s,}" % count, string)

# [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of
# those characters, in any order, but only once each.

# [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English
# alphabet in lowercase, uppercase, or both upper and lowercases.

# [0-9] - range that'll match any number from 0 to 9. You can change the ends
# to restrict the set.

def find_emails(string):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', string)

# Create a variable named good_numbers that is an re.findall() where the pattern
# matches anything in string except the numbers 5, 6, and 7.
string = '1234567890'
good_numbers = re.findall(r'[^5-7]', string)
print good_numbers # ['1', '2', '3', '4', '8', '9', '0']
