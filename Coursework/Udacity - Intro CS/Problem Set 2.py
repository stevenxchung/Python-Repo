# ~~~~~ Problem 1 ~~~~~
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

def udacify(s):
    return 'U' + s

# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat



# ~~~~~ Problem 2 ~~~~~
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if a == big:
        return bigger(b,c)
    elif b == big:
        return bigger(a,c)
    else:
        return bigger(a,b)

#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7



# ~~~~~ Problem 3 ~~~~~
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    while n > 0:
        print n
        n=n-1
    print "Blastoff!"

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!



# ~~~~~ Problem 4 ~~~~~
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search,target):
    last = -1
    while True:
        current = search.find(target,last+1)
        if current == -1:
            return last
        last = current

#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0
