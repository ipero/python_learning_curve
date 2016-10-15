# Things you can do with funcitons:

# --- 1 --- call one funcitons in athorer function
def first(n):
    return n + 1

def second(n):
    return first(n) + 2
print second(30) # it prints 33

# same thing here
def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print by_three(9)
print by_three(5)

# --- 2 --- import particular funciton from module
from math import sqrt
print sqrt(25)

# --- 3 --- universal import (imports all variables and functions)
#  !!! This practice is dangeres!!!
# it can over write variables and functions with same name.
from math import *
print fabs(-50) # prints float absolute value 50.0

# --- 4 --- Python has many built in funcitons, for example type
# type() returns the type of variable
print type(432) # prints <type 'int'>
print type(5.5) # prints <type 'float'>
print type("Hello") # prints <type 'str'>
arr = (2, 4, 56)
print type(arr) # prints <type 'list'>
