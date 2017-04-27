#chapter 7 exercises
#####################

# 3 - Write a function which is given an exam mark, and it returns the corresponding letter
#grade as a string according to this scheme:
# >= 90  >>> "A"
# [80 - 90)  >>> "B"
# [70 - 80)  >>> "C"
# [60 - 70)  >>> "D"
# <60  >>> "F"

#####################
def what_grade(num_grade):
    if num_grade >= 90:
        return "A"
    elif num_grade < 90 and num_grade >= 80:
        return "B"
    elif num_grade < 80 and num_grade >= 70:
        return "C"
    elif num_grade < 70 and num_grade >= 60:
        return "D"
    else:
        return "F"
#######################
# test cases and expected output
print(what_grade(91)) # A
print(what_grade(80)) # B
print(what_grade(89.9999)) # B
print(what_grade(72)) # C
print(what_grade(79)) # C
print(what_grade(70)) # C
print(what_grade(64)) # D
print(what_grade(60)) # D
print(what_grade(45)) # F
print(what_grade(2)) # F
print(what_grade(59.995)) # F

########################

# 4 -Write a function findHypot. The function will be given the length of two sides of a
#right-angled triangle and it should return the length of the hypotenuse

########################
def findHypot(a,b):
    return (a ** 2 + b ** 2)** 0.5
########################
# test cases and expected results
findHypot(12.0, 5.0) # 13.0
findHypot(14.0, 48.0) # 50.0
findHypot(21.0, 72.0) # 75.0
findHypot(1, 1.73205) # 1.999999
#########################

# 7 - Write a function called is_even(n) that takes an integer as an argument and returns
#True if the argument is an even number and False if it is odd.

#########################
def is_even(n):
    return n % 2 == 0
#########################
# test cases and expected results
is_even(10) # True
is_even(5) # False
is_even(1) #False
is_even(0) #True
#########################

# 8 - Write the function is_odd(n) that returns True when n is odd and False otherwise.

#########################
def is_odd(n):
    return n % 2 > 0
#########################
# test cases and expected results
is_odd(10) # False
is_odd(5) # True
is_odd(1) # True
is_odd(0) # False
##########################

#Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.

###########################
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return (not is_even(n))
############################
#test cases and expected results
is_odd(10), #False
is_odd(5)  #True
is_odd(1) #True
is_odd(0) #False
#############################

#10 - Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled. Assume that the third argument
# to the function is always the longest side. It will return True if the triangle is
# right-angled, or False otherwise.

#############################
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
#############################
# test cases and expected results
is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(4.0, 8.0, 16.0) #False
is_rightangled(4.1, 8.2, 9.1678787077) #True
is_rightangled(4.1, 8.2, 9.16787) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.4, 0.64031) #True
##############################

# 11 - Extend the above program so that the sides can be given to the function
# in any order.

#############################
def is_rightangled(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
############################
# test cases and expected results
is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(16.0, 4.0, 8.0) #False
is_rightangled(4.1, 9.1678787077, 8.2) #True
is_rightangled(9.16787, 4.1, 8.2) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.64031, 0.4) #True
##############################
year = int(input("Please enter a year between 1900-2099 to find out the date of Easter for that year"))
if year >= 1900 and year <= 2099:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        dateofeaster = dateofeaster - 7

    if dateofeaster > 31:
        print("April", str(dateofeaster - 31) + ",", year)
    else:
        print("March", str(dateofeaster) + ",", year)
else:
    print("Error: Invalid year.  Please enter a year between 1900 and 2099")
