import re

names_file = open("names.txt")
data = names_file.read()
names_file.close()

# r - raw string
# match - find match at the beginning of string
# search - search entire file
# print(re.match(r'Ryan', data))
# print(re.search(r'Chalkley', data))

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


# ([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'.
# This could be later accessed from the Match object as .group(1)
#
# (?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'.
# This could later be accessed from the Match object as .group('name').
#
# .groups() - method to show all of the groups on a Match object.
#
# re.MULTILINE or re.M - flag to make a pattern regard lines in your text
# as the beginning or end of a string.
#
# ^ - specifies, in a pattern, the beginning of the string.
#
# $ - specifies, in a pattern, the end of the string.

# ------------------------------------------------------------------------------
# Create a variable names that is an re.match() against string. The pattern should
# provide two groups, one for a last name match and one for a first name match.
# The name parts are separated by a comma and a space.

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
    (?P<last>[\w]+),\s
    (?P<first>[\s\w]+)
''', string, re.X)

print names.groups()

# ------------------------------------------------------------------------------

# Create a new variable named contacts that is an re.search() where the pattern
# catches the email address and phone number from string. Name the email pattern
# email and the phone number pattern phone.

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
     ,\s
     (?P<phone>\d{3}-\d{3}-\d{4})'''
     , string, re.X | re.M)

twitters = re.searcch(r'''
    (?P<twitter>@[^t][\w\d]+) '''
    , string, re.X | re.M)

print contacts.groups()

# ------------------------------------------------------------------------------

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    (?P<last_name>[\w ]+),
    \s(?P<first_name>[\w ]+):\s(?P<score>[\d]+)
''', string, re.M)
