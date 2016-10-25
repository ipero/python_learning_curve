# Write a function called digit_sum that takes a positive integer num as input
# and returns the sum of all that number's digits.
def digit_sum(num):
    digit_sum = 0
    number = str(num)
    for digit in number:
        digit_sum += int(digit)

    return digit_sum

print digit_sum(1234)

# find factorial of positive number
def factorial(n):
    factorial = 1
    if n == 0:
        return factorial
    for i in range(n, 0, -1):
        factorial *= i
    return factorial
print factorial(4)

# find if number is prime number (can be divided even by itself of 1)
# 2, 3, 5, 7 and 11 are prime numbers
def is_prime(num):
    result = True
    if num > 1:
        for n in range(2, num):
            print n
            if num % n == 0:
                result = False
                break
    else:
        result = False
    return result
print is_prime(2)

# function that returns reversed string without using reversed or [:: -1]
def reverse(text):
    reverse = ""
    letters = list(text)
    for i in range(len(letters)-1, -1, -1):

        reverse += letters[i]

    return reverse

print reverse("banana and apple")

# remove vowels "a, e, i, o, u" (keep "y")
def anti_vowel(text):
    no_vowels = ""
    for c in text:
        if c == "a" or c == "A":
            no_vowels += ""
        elif c == "o" or c == "O":
            no_vowels += ""
        elif c == "e" or c == "E":
            no_vowels += ""
        elif c == "i" or c == "I":
            no_vowels += ""
        elif c == "u" or c == "U":
            no_vowels += ""
        else:
            no_vowels += c
    return no_vowels
print anti_vowel("It is my text")

# find scrabble score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total_score = 0
    word = word.lower()
    for c in word:
        total_score += score.get(c, 0)
    return total_score
print scrabble_score("Helix ")
