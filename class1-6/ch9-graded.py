# Chapter 9 Graded Assignment
############################

#Write a function that mirrors its argument. For example, mirror('good')
#should return a string holding the value gooddoog. (Hint: Make use of
#the reverse function that you wrote in the previous exercise.)

############################
def reverse(text):
    '''Takes a string as a parameter, and returns the string in complete reverse order'''
    backwards = ''
    for char in text:
           backwards = char + backwards
    return backwards
def mirror(text):
    '''Takes a string as a parameter and returns the string, along with a mirror image of the string'''
    return text+reverse(text)
