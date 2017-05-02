#####################
# Bonus 1 - class 5/1 - Write a function that takes in a float and returns the number
# of digits that occur after the decimal point.
#####################

from test import testEqual
def digit_count(flt):
    my_float = str(flt)
    decimal = my_float.find(".")
    if decimal == -1:
        return 0
    return len(my_float[decimal + 1:])

testEqual(digit_count(3.14), 2)
testEqual(digit_count(9.876543), 6)
testEqual(digit_count(9825), 0)
########################
#Solution using for loop:
def digit_count(flt):
    my_float = str(flt)
    for char in range(len(my_float)):
        if my_float[char] == ".":
            return len(my_float[char + 1 : ])
    return 0
#########################
