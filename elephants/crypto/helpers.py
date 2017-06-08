import string

def alphabet_position(letter):
	'''Takes a single letter, and returns a value between 0-25 based 
	on the letters position in the alphabet'''
	lower = string.ascii_lowercase
	lowerletter = letter.lower()
	return lower.index(lowerletter)

def rotate_character(char, rot):
	'''Takes a single character and a rotation number.  Returns the character 
	equivalent to the letters original position in the alphabet plus the rotation value'''
	new_char = ""
	if char.isalpha() == False:
		return char
	index = (alphabet_position(char) + rot) % 26
	if char.islower():
		new_char = string.ascii_lowercase[index]
	else:
		new_char = string.ascii_uppercase[index]
	
	return new_char