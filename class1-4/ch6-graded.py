# chapter 6 graded assignment
##########################

#Write a function isLeap that takes a single parameter, year.  The function
#should return True if the year is a leap year, and False if the year is not
#a leap year.

##########################
def isLeap(year):
    # your code here
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

#############################
#test cases and expected results
isLeap(1944) # True
isLeap(2011) #False
isLeap(1986) #False
isLeap(1956) #True
isLeap(1957) #False
isLeap(1800) #False
isLeap(1900) #False
isLeap(1600) #True
isLeap(2056) #True
