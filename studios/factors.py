# bonus studio for may 15
##########################33
# Create a function factors that takes in an integer n and generates 
# a dictionary that contains the factors of all values from 1 to n.
def factors(n):
	'''Takes an integer n and returns a dictionary that contains the 
	factors of all values from 1 to n.'''
	#create empty list
	facts = {}
	#create keys for range 1-n inside list
	for num in range(1, n + 1):
		facts[num] = []
	#loop through range again, and each key in dictionary.  if the element 
	#is cleanly divisible by the index, add index as the value to key.
	for num in range(1, n + 1):
		for key in facts:
			if key % num == 0:
				facts[key] = facts[key] + [num]
	return facts

def main():
	input_num = int(input("Pick a number:\n"))
	print("The factors of", input_num, "are:", factors(input_num))

if __name__ == '__main__':
	main()

