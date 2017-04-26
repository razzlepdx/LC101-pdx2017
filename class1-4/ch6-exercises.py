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



###########################
