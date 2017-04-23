#Ch 4 Graded Assignment

#Assume you have the list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#write a loop that prints each of the numbers on a new line
#write a second loop that prints each number and it's square on a new line, ex: The square of 12 is
#144 \n the square of 10 is 100, etc
################

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in nums:
  print(num)

for num in nums:
  print("The square of", num, "is", (num**2))
