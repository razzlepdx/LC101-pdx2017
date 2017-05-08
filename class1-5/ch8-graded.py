#Chapter 8 graded assignment
########################
#Write a function analyze_text that receives a string as input. Your function should
#count the number of alphabetic characters (a through z, or A through Z) in the text
#and also keep track of how many are the letter 'e' (upper or lowercase).

#Your function should return an analysis of the text, something like this:
#The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.
########################
def analyze_text(text):
    count = 0
    e_count = 1
    for char in text:
        if char.isalpha == True:
            count = count + 1
        if char == 69 or char == 101:
            e_count = e_count + 1
        if e_count == 0:
            percent = 100
        else:
            print(type(char), "failed this loop")
    return "The text contains", count, "alphabetic characters, of which", e_count - 1, "(" + str(count/e_count) + "%) are 'e'."
##########################
