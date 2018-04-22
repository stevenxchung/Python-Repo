# ~~~~~ Problem 1 ~~~~~
# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    return product if set(product) <= set(debris) \
                   else "Give me something that's not useless next time."


### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'



# ~~~~~ Problem 2 ~~~~~
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

"""
def days(month1, month2)

    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_months = 0
    delta_months = abs(month2 - month1)

    while delta_months > 0:
        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7,
        or month1 == 8 or month1 == 10 or month1 == 12:
            days_in_months = 31
        elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
            days_in_months = 30
        else:
            days_in_months = 28
        ...

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    leap_day = 0
    leap_year = year1
    delta_years = year2 - year1
    while delta_years > 0:
        if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
            leap_day = leap_day + 1
            leap_year = leap_year + 1
            delta_years = delta_years - 1
        else:
            leap_year = leap_year + 1
            delta_years = delta_years - 1
        return leap_day

    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_years = (year2 - year1)
    total_days_in_months = sum(daysOfMonths[month1-1:month2-1])

    total_days = total_years * 365 + total_days_in_months + abs(day2 - day1) + leap_day

    return total_days
"""

def days_in_month(n):
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][n-1]

def leap_days(month, day, year):
    days = 365
    #now need to do if it is leap year
    if (year % 4 == 0) and (year % 100 != 0) and (month > 2):
        days = days + 1
    return days

def days_since_0(month, day, year):
    days = year * 365 + day
    for n in range(1, month):
        days = days + days_in_month(n)
    return days + leap_days(month,day,year)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    return days_since_0(month2, day2, year2) - days_since_0(month1, day1, year1)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

# ~~~~~ Problem 3 ~~~~~
#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    for i in range(0, 10):
        print "|00000*****|"[: - (int(('0' * (10 - len(str(value))) + str(value))[i]) + 1)] \
        + '   ' + "|00000*****|"[ - (int(('0' * (10 - len(str(value))) + str(value))[i]) + 1):]

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|



# ~~~~~ Problem 4 ~~~~~
# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.

def jungle_animal(animal, my_speed):
    if animal == 'zebra':
        print "Try to ride a zebra!"
    elif animal == 'cheetah':
        if my_speed > 115:
            print "Run!"
        else:
            print "Stay calm and wait!"
    else:
        print "Introduce yourself!"

#jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

#jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"



# ~~~~~ Problem 5 ~~~~~
# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).

def is_leap_baby(day,month,year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and (day == 29 and month == 2):
        return True
    else:
        return False

# The function 'output' prints one of two statements based on whether
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!
