from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
	'''Takes an input string and a rotation number.  Returns a string where 
	each character has been shifted forward through the alphabet by the 
	amount specified in the rotation number'''
	
	#create a variable to hold the encrypted message
	new_text = ''

	#loop over each character in the text input
	for i in range(len(text)):
		#rotate each character by the rotation value, then push to return string
		new_text += rotate_character(text[i], rot)

	return new_text

def main():
	from sys import argv
	if (len(argv) == 1):
		aMessage = input("Type a message:\n")
		myRot = int(input("Rotate characters by:\n"))
		print(encrypt(aMessage, myRot))

	elif (len(argv) > 2) or (argv[1].isdigit() == False):
		print("usage: python caesar.py n\nArguments:\n-n: The number to be used as the rotation value to encrypt your message.  Should only contain whole numbers - no decimals, letters, or special characters")
		exit()
	else:
		aMessage = input("Type a message:\n")
		print(encrypt(aMessage, int(argv[1])))

if __name__ == '__main__':
	main()