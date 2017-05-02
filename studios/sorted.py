#Studio for class 5-1
#####################
#Write a function which returns a boolean indicating if the string is sorted or not.
####################

from test import testEqual
def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    for char in range(len(string) - 1):
        if string[char] > string[char + 1]:
            return False

    return True


testEqual(is_sorted("ABC"),True)
testEqual(is_sorted("aBc"),False)
testEqual(is_sorted("dog"),False)
