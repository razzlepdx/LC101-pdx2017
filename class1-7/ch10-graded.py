# Chapter 10 graded assignment
###########################
# Define a function called sum_evens, which receives one argument, 
# a list of numbers.  Your function should return the sum of all the
# even numbers in the list
###########################
def sum_evens(nums):
    total = 0
    for anum in nums:
        if anum % 2 == 0:
            total += anum
    return total
