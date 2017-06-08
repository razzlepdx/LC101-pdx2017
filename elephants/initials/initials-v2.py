def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    names = fullname.split(' ')
    inits = ''
    for name in names:
    	inits += name[0]
    return inits.upper()

print(get_initials("rachel E Wilson"))

def get_initials_two(fullname):
	inits = ''
	for ind, char in enumerate(fullname):
		if ind == 0:
			inits += char.upper()
		elif fullname[ind] == " ":
			inits += fullname[char + 1].upper()

print(get_initials_two("rachel e Wilson"))