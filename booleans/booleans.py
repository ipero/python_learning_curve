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


# is circus ofpen
def is_circus_open(clown, weather):
    if (clown == True and (weather == "sunny" or weather == "cloudy")):
        print "Circus is open!!!"
        return True
        # the code inside this block!
    elif clown == True and weather == "rainy":
        print "Sorry, we are closed today."
        return False
    elif clown == False:
        print "Sorry, we are out of clowns!"
        return False
    else:
        print "Nothing matches your inputs"
        return False
is_circus_open(True, "sunny")
is_circus_open(True, "cloudy")
is_circus_open(True, "rainy")
is_circus_open(False, "sunny")
