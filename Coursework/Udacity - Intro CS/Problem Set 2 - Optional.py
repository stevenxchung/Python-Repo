# ~~~~~ Problem 1 ~~~~~
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False



# ~~~~~ Problem 2 ~~~~~
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(n):
    p5 = n/5
    p2 = (n - 5*p5)/2
    p1 = n - 5*p5 - 2*p2

    return p5, p2, p1

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps



# ~~~~~ Problem 3 ~~~~~
# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def bigger(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def biggest(n1,n2,n3):
    return bigger(bigger(n1,n2),n3)

def smaller(n1,n2):
    if n1 < n2:
        return n1
    else:
        return n2

def smallest(n1,n2,n3):
    return smaller(smaller(n1,n2),n3)

def set_range(n1,n2,n3):
    big = biggest(n1,n2,n3)
    small = smallest(n1,n2,n3)
    return big - small

#print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

#print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
