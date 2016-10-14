# This is an order of operations for boolean operators:
#
# 1. not is evaluated first;
# 2. and is evaluated next;
# 3. or is evaluated last.

bool_one = False or not True and True
print bool_one # False

bool_two = False and not True or True
print bool_two # True

bool_three = True and not (False or False)
print bool_three # True

bool_four = not not True or False and not True
print bool_four # True

bool_five = False or not (True and True)
print bool_five # False

# Make me false!
bool_six = (2 <= 2) and "Alpha" == "Bravo"
print bool_six

# Make me true!
bool_seven = not 20 == 3*10 and 3*4 <= 4*3 or 4**2 !=116 % 100
print bool_seven

# Make me false!
bool_eight = not not 2**3 != 2*3 and 12 % 6 == 1**0
print bool_eight

# Make me true!
bool_nine = 4 % 3 == 0**0 and 2**5 >= 6*5
print bool_nine

# Make me true!
bool_ten = not(2*2+2 != 3*3-3) and 17 % 4 != 4*4
print bool_ten


# Make sure that the_flying_circus(clown,weather) returns True
def the_flying_circus():
    if ________:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
    elif ________:
        # Keep going here.
        # You'll want to add the else statement, too!
