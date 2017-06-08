from helpers import alphabet_position, rotate_character

def encrypt(text, keyword):
	'''Takes a string and encryption keyword, and returns a new string transformed 
	by the individual letter values of the keyword'''
	
	#create variables to hold encrypted message and keyword position values
	new_text = ''
	pos = 0

	#loop over each character in text input
	for index in range(len(text)):
		#check for alpha characters, then rotate by keyword[index], increment key position, 
		#and push encrypted character to return string
		if text[index].isalpha():
			key = alphabet_position(keyword[pos])
			new_text += rotate_character(text[index], key)
			pos = (pos + 1) % len(keyword)
		#for non-alpha characters, push to return string unchanged
		else:
			new_text += text[index]

	return new_text

def main():
	from sys import argv, exit
	if (len(argv) == 1):
		aMessage = input("Type a message:\n")
		myKey = input("Type a keyword:\n")
		print(encrypt(aMessage, myKey))

	elif (len(argv) > 2) or (argv[1].isalpha() == False):
		print("usage: python vigenere.py keyword\nArguments:\n-keyword: The string to be used as the 'key' to encrypt your message.  Should only contain alphabetic characters - no numbers or special characters.")
		exit()
	else:
		aMessage = input("Type a message:\n")
		print(encrypt(aMessage, argv[1]))

if __name__ == '__main__':
	main()