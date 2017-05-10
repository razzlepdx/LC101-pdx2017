# chapter 10 practice exercises - prep for class 5/8/17
##########################

#2 - Create a list called myList with the following six items: 76, 92.3, “hello”, 
# True, 4, 76. Do it with both append and with concatenation, one item at a time.

##########################
myList = []

myList.append(76)
myList.append(92.3)
myList += ["hello"]
myList += [True]
myList.append(4)
myList += [76]

print(myList)

###########################

# 3 - Starting with myList from #2, write Python statements to do the following:


###########################
# Append “apple” and 76 to the list.

myList.append('apple', 76)

# Insert the value “cat” at position 3.

myList.insert(3, 'cat')

# Insert the value 99 at the start of the list

myList.insert(0, 99)

# Find the index of “hello”.

myList.index("hello")

# Count the number of 76s in the list.

myList.count(76)

# Remove the first occurrence of 76 from the list.

myList.remove(76)

# Remove True from the list using pop and index.

myList.pop(myList.index(True))

#############################

# 4 - Write a function to coount how many odd numbers are in a list

##############################

def num_of_odd(list):
	count = 0
	for anum in list:
		if anum % 2 != 0:
			count += 1
	return count

###############################

