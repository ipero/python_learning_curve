# Something completely different about Python is the while/else construction.
# while/else is similar to if/else, but there is a difference: the else block
# will execute anytime the loop condition is evaluated to False. This means
# that it will execute if the loop is never entered or if the loop exits normally.
# If the loop exits as the result of a break, the else will not be executed.
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win"
        break
    guesses_left -= 1
else:
    print "You lose."

# Just like with while, for loops may have an else associated with them.

#In this case, the else statement is executed after the for, but only
# if the for ends normally—that is, not with a break. This code will break
# when it hits 'cart', so the else block won't be executed.
cars = ["Ford", "Chevy", "VW", "BMW", "Audi", "cart", "Volvo", "Honda"]

print "Popular cars:"
for car in cars:
    if car == "cart":
        print "Cart is not a car!"
        break
    print car
else:
    "This was a list of popular cars"
