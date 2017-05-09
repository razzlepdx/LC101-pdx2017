#Stretch studio for class 5-4
#############################
#Write a function called stretch that takes in a string and doubles each
# of the letters contained in the string.  Add an optional parameter to 
#your stretch function that indicates how many times each letter should 
#be duplicated. The default value for this optional parameter should be 2.
# Add an additional optional parameter to your stretch function that contains 
#a list of characters. This version of stretch will only duplicate letters 
#that are contained in the list. The default value for this new parameter 
#should be the list of lowercase characters.
##############################

def stretch(str, repeat=2, dups=''):
    new_str = ''
    #iterate over input string
    for letter in str:
        if len(dups) > 0:
            #check to see if current letter is part of 3rd parameter
            if dups.find(letter) != -1:
                #if so, repeat letter by repeat value and transfer to new string
                new_str += letter * repeat
            else:
                #if not, transfer letter to new string once (no repeat)
                new_str += letter
    
    return new_str