# Things you can do with funcitons:

# call one funcitons in athorer function
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
