# 2 - Write a function that will return the number of digits in an integer.
##########################
def num_of_digits(n):
    n = str(n)
    return len(n)
##########################
#tests and expected reponses
def main():
    print(num_of_digits(0)) #1
    print(num_of_digits(14)) # 2
    print(num_of_digits(7)) #1
    print(num_of_digits(146)) # 3
    print(num_of_digits(9076)) # 4
    print(num_of_digits(56732)) # 5
    print(num_of_digits(353535)) # 6
    print(num_of_digits(5789086)) #7

main()
#########################

# 3- Write a function that removes all occurrences of a given letter from a string.

#########################
def remove_letter(theLetter, theString):
    return theString.replace(theLetter, "")
##########################
#tests and expected results
def main():
    remove_letter('a', 'apple') # 'pple'
    remove_letter('a', 'banana') # 'bnn'
    remove_letter('z', 'banana') # 'banana'

main()
##########################

# 4- Write a function that removes the first occurrence of a string from another string.

##########################
def remove(substr,theStr):
    '''Removes the first occurence of a substring from another string'''
    return theStr.replace(substr, "", 1)
##########################
#tests and expected results
def main():
    remove('an', 'banana') # 'bana'
    remove('cyc', 'bicycle') # 'bile'
    remove('iss', 'Mississippi') # 'Missippi'
    remove('egg', 'bicycle') # 'bicycle'
    remove('oo', 'Yahoohoo' # 'Yahhoo'

main()
##########################

# 5 - Write a function that removes all occurrences of a string from another string.

##########################
def remove_all(substr,theStr):
    return theStr.replace(substr, "")
##########################
# tests and expected results
def main():
    remove_all('an', 'banana') # 'ba'
    remove_all('cyc', 'bicycle') # 'bile'
    remove_all('iss', 'Mississippi') # 'Mippi'
    remove_all('eggs', 'bicycle') # 'bicycle'

main()
###########################
