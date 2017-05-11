# Chapter 11 exercises - for class may 11
##############################

# 1 - Create a list containing 100 random integers between 0 and 1000 (use 
# iteration, append, and the random module). Write a function called average 
# that will take the list as a parameter and return the average.

##############################
import random

somenums = []

for a in range(100):
    somenums.append(random.randrange(0,1000))

def average(numlist):
    averagesum = 0
    for num in numlist:
        averagesum += num
    return averagesum/100

print(average(somenums))
###############################

# 2 - Write a Python function that will take a the list of 100 random integers 
# between 0 and 1000 and return the maximum value

###############################
import random

somenums = []

for a in range(100):
    somenums.append(random.randrange(0,1000))

def maxnum(numlist):
    larger = 0
    for num in numlist:
        if num > larger:
            larger = num
    return larger
###############################
# 3 - Write a function sum_of_squares(xs) that computes the sum of the squares of 
# the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 
# 4+9+16 which is 29

###############################
def sum_of_squares(xs):
    sum = 0
    for item in xs:
        sum += item**2
    return sum
###############################

# 4 - Sum up all the negative numbers in a list.

###############################

myList = [5, 6, -8, -34, 56, -2.33]

def neg_total(lst):
    neg_sum = 0
    for number in lst:
        if number < 0:
            neg_sum += number
    return neg_sum

print(neg_total(myList))
###############################

# 5 - Count how many words in a list have length 5. 

###############################
mywords = ['words', 'list', 'chive', 'alive', 'subtle', 'python', 'foo', 'bar']

def countfive(wrdlst):
    counter = 0
    for aword in range(len(wrdlst)):
        if len(wrdlst[aword]) == 5:
            counter += 1
    return counter
#################################

# 6 - Count how many words occur in a list up to and including the first 
# occurrence of the word “sam”

##################################
def findsam(lst):
    return (lst.index("sam") + 1)
##################################

# 7 - Although Python provides us with many list methods, it is good practice 
# and very instructive to think about how they are implemented. Implement a 
# Python function that works like the following:

# in
# reverse
# index
# insert

###################################
#count

def countme(xlist, yitem):
    counter = 0
    for item in xlist:
        if item == yitem:
            counter+=1
    return counter

# in

def in_it(xlist, yitem):
    for item in xlist:
        if item == yitem:
            return True
    return False

# reverse

def rvrs(xlist):
    backwards = []
    for item in range(len(xlist)):
        backwards = [xlist[item]] + backwards
    return backwards

# index

def findindex(xlist, yitem):
    for ind in range(len(xlist)):
        if xlist[ind] == yitem:
            return ind
    return -1

# insert

def insert(xlist, yitem, zpos):
    new_list = []
    for ind in range(len(xlist)):
        if ind < zpos:
            new_list.append(xlist[ind])
        elif ind == zpos:
            new_list.append(yitem)
            for item in range(zpos, len(xlist[zpos:])+ 1):
                new_list.append(xlist[item])
        
    return new_list


###################################

# 8 - Write a function replace(s, old, new) that replaces all occurences of old 
# with new in a string s:

###################################