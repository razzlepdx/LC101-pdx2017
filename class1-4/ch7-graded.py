#chapter 7 graded assignment
#########################

# Define a function is_prime, that takes a single integer argument
# and returns True when the argument is a prime number and False otherwise

##########################
def is_prime(x):
    divisible = 0
    for i in range(2,x):
        if x % i == 0:
            divisible += 1
    if divisible > 0 and x != 2:
        return False
    else:
        return True
