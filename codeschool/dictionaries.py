# We want to print a big vertical Welcome sign for our circus, and to do that
# we want to print each letter of 'Welcome!' on a separate line. We can do
# this with a for loop — for each letter in our word, we'll print it.
word = 'Welcome!'
for char in word:
    print (char)


# Let's help the fortune-teller robot generate random lotto ticket suggestions
# for its customers. We'll use a for loop to pick five random numbers between 1 and 53.
import random

for i in range(5):
    print (random.randint(1,53))

# We want to print out a schedule of our circus' performances. To do this,
# we can take our dictionary of performances and print out each item
# on a separate line using a for loop.
performances = {'Ventriloquism':'9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Enchanted Elephants':'5:00pm'}
for key, value in performances.items():
    print (key, ": ", value, sep="")

# We want to create a "guess the number" game for our fortune-teller robot.
# If you guess the random number between 1 and 10, you win a crystal ball!

guess = int(input('Guess a number between 1 and 10'))
times = 1
while guess != num:
    guess = int(input('Guess again'))
    times = times + 1
    if times == 3:
        break
if guess == num:
    print('You win!')
else:
    print ("You lose! The number was," num)
