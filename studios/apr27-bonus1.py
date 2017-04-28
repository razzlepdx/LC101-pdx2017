#Bonus task from class Apr27:
#Write a function that takes in an integer then displays the multiplication table of that size.
#For example, if the given integer was 3, the following multiplication table would be displayed:

# 0 0 0 0
# 0 1 2 3
# 0 2 4 6
# 0 3 6 9

#solution worked out with help from Dina Moy
#####################

number = int(input("Give me a number!"))

col = range(0,number+1)
row = range(0,number+1)

for r in row:
   for c in col:
       print((r*c),end="\t")
   print("")

#####################
