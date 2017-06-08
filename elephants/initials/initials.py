# Unit 1 initials assignment
#############################

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    inits = ''
    for char in range(len(fullname)):
    	if char == 0 or fullname[char-1] == " ":
    		inits += fullname[char].upper()
    return ("The initials of " + fullname + " are " + inits)

def main():
	''' Prompts the user for an input string and returns the result of get_initials(userinput)'''
	get_name = input("What is your full name?\n")
	print(get_initials(get_name))

if __name__ == '__main__':
	main()

##################

