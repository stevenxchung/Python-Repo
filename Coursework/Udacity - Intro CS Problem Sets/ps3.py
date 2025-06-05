# ~~~~~ Problem 1 ~~~~~
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(list_of_numbers):
    i = 0
    prod = 1
    while i < len(list_of_numbers):
        prod = prod * list_of_numbers[i]
        i += 1
    return prod


print(product_list([9]))
# >>> 9

print(product_list([1, 2, 3, 4]))
# >>> 24

print(product_list([]))
# >>> 1


# ~~~~~ Problem 2 ~~~~~
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(list_of_numbers):
    p = list_of_numbers
    big = 0
    for e in p:
        if e > big:
            big = e
    return big


print(greatest([4, 23, 1]))
# >>> 23
# print greatest([])
# >>> 0


# ~~~~~ Problem 3 ~~~~~
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string,
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500],
]


def total_enrollment(listE):
    totalStudents = 0
    totalTuition = 0
    for name, students, tuition in listE:
        totalStudents += students
        totalTuition += tuition * students
    return totalStudents, totalTuition


print(total_enrollment(udacious_univs))
# >>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside
# interpreter you might not see it.

# print total_enrollment(usa_univs)
# >>> (77285,3058581079)


# ~~~~~ Problem 4 ~~~~~
# The web crawler we built at the end of Unit 3 has some serious
# flaws if we were going to use it in a real crawler. One
# problem is if we start with a good seed page, it might
# run for an extremely long time (even forever, since the
# number of URLS on the web is not actually finite). This
# question and the following one explore two different ways
# to limit the pages that it can crawl.

# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.

# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return (
                '<html> <body> This is a test page for learning to crawl! '
                '<p> It is a good idea to '
                '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                'crawl</a> before you try to  '
                '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                '</p> </body> </html> '
            )
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return (
                '<html> <body> I have not learned to crawl yet, but I '
                'am quite good at '
                '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                '</body> </html>'
            )
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return (
                '<html> <body> I cant get enough '
                '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                '</body> </html>'
            )
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return (
                '<html> <body> The magic words are Squeamish Ossifrage! '
                '</body> </html>'
            )
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


# Modify the crawl_web procedure to take a second parameter,
# max_pages, that limits the number of pages to crawl.
# Your procedure should terminate the crawl after
# max_pages different pages have been crawled, or when
# there are no more pages to crawl.


def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if (page not in crawled) and (len(crawled) < max_pages):
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


# print crawl_web("http://www.udacity.com/cs101x/index.html",1)
# >>> ['http://www.udacity.com/cs101x/index.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",3)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",500)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html',
# >>> 'http://www.udacity.com/cs101x/crawling.html',
# >>> 'http://www.udacity.com/cs101x/kicking.html']


# ~~~~~ Problem 5 ~~~~~
#
# This question explores a different way (from the previous question)
# to limit the pages that it can crawl.
#
#######

# THREE GOLD STARS #
# Yes, we really mean it!  This is really tough (but doable) unless
# you have some previous experience before this course.


# Modify the crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.
#
# For example, if max_depth is 0, the only page that should
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that
# it links to directly. If max_depth is 2, the crawl should
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface
# to the website found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return (
                '<html> <body> This is a test page for learning to crawl! '
                '<p> It is a good idea to '
                '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                'crawl</a> before you try to  '
                '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                '</p> </body> </html> '
            )
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return (
                '<html> <body> I have not learned to crawl yet, but I '
                'am quite good at '
                '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                '</body> </html>'
            )
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return (
                '<html> <body> I cant get enough '
                '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                '</body> </html>'
            )
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return (
                '<html> <body> The magic words are Squeamish Ossifrage! '
                '</body> </html>'
            )
        elif url == "http://top.contributors/velak.html":
            return (
                '<a href="http://top.contributors/jesyspa.html">'
                '<a href="http://top.contributors/forbiddenvoid.html">'
            )
        elif url == "http://top.contributors/jesyspa.html":
            return (
                '<a href="http://top.contributors/elssar.html">'
                '<a href="http://top.contributors/kilaws.html">'
            )
        elif url == "http://top.contributors/forbiddenvoid.html":
            return (
                '<a href="http://top.contributors/charlzz.html">'
                '<a href="http://top.contributors/johang.html">'
                '<a href="http://top.contributors/graemeblake.html">'
            )
        elif url == "http://top.contributors/kilaws.html":
            return (
                '<a href="http://top.contributors/tomvandenbosch.html">'
                '<a href="http://top.contributors/mathprof.html">'
            )
        elif url == "http://top.contributors/graemeblake.html":
            return (
                '<a href="http://top.contributors/dreyescat.html">'
                '<a href="http://top.contributors/angel.html">'
            )
        elif url == "A1":
            return '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += 1
    return crawled


# print crawl_web("http://www.udacity.com/cs101x/index.html",0)
# >>> ['http://www.udacity.com/cs101x/index.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",1)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html',
# >>> 'http://www.udacity.com/cs101x/crawling.html']

# print crawl_web("http://www.udacity.com/cs101x/index.html",50)
# >>> ['http://www.udacity.com/cs101x/index.html',
# >>> 'http://www.udacity.com/cs101x/flying.html',
# >>> 'http://www.udacity.com/cs101x/walking.html',
# >>> 'http://www.udacity.com/cs101x/crawling.html',
# >>> 'http://www.udacity.com/cs101x/kicking.html']

# print crawl_web("http://top.contributors/forbiddenvoid.html",2)
# >>> ['http://top.contributors/forbiddenvoid.html',
# >>> 'http://top.contributors/graemeblake.html',
# >>> 'http://top.contributors/angel.html',
# >>> 'http://top.contributors/dreyescat.html',
# >>> 'http://top.contributors/johang.html',
# >>> 'http://top.contributors/charlzz.html']

# print crawl_web("A1",3)
# >>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)


# ~~~~~ Problem 6 ~~~~~
# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

incorrect = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

incorrect3 = [
    [1, 2, 3, 4, 5],
    [2, 3, 1, 5, 6],
    [4, 5, 2, 1, 3],
    [3, 4, 5, 2, 1],
    [5, 6, 4, 3, 2],
]

incorrect4 = [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b']]

incorrect5 = [[1, 1.5], [1.5, 1]]


def check_sudoku(inputList):
    lenA = len(inputList)
    # Loop through the entire matrix, checking if digit > lenA
    for digit in range(1, lenA + 1):
        # Loop through each row denoted by index i, need i = 0 for reset
        i = 0
        for i in range(lenA):
            # Loop through each column denoted by index j, need j = 0 for reset
            # Also need row and columns indexed to 0 for reset
            row_count = 0
            col_count = 0
            j = 0
            for j in range(lenA):
                # Check if digit only occurs once
                if inputList[i][j] == digit:
                    row_count += 1
                if inputList[j][i] == digit:
                    col_count += 1
            if row_count != 1 or col_count != 1:
                return False
    return True


print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
