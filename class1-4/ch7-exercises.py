# 2 - Write a function print_triangular_numbers(n) that prints out the first
# n triangular numbers. A call to print_triangular_numbers(5) would
# produce the following output:
#1       1
#2       3
#3       6
#4       10
#5       15

#########################
def print_triangular_numbers(x):
    sum = 0
    for num in range(1, x+1):
        sum += num
        print(num, "\t", sum)
#########################
#most of the rest of these exercises were for turtles or image processing.
#These are best practiced inside the textbook.  
