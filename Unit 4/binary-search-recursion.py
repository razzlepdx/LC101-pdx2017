def binary_search(goal, list_of_crap):
    first = 0
    last = len(list_of_crap) - 1 
    
    # base conditional 1
    if last < first:
        return "That thing isn't here"
    
    midpoint = (first + last) // 2
    guess = list_of_crap[midpoint]
    
    # base conditional 2
    if guess == goal:
        return "Found it!"
    
    # recursive conditionals    
    if guess < goal:
        list_of_crap = list_of_crap[(midpoint + 1):]
        return binary_search(goal, list_of_crap)
    
    if guess > goal:
        list_of_crap = list_of_crap[0:midpoint]
        return binary_search(goal, list_of_crap)

print(binary_search(4, [1,2,3,4,5,6,7,8,9,10,11,12]))
print(binary_search(-1, [1,2,3,4,5,6,7,8,9,10,11,12]))
print(binary_search(14, [1,2,3,4,5,6,7,8,9,10,11,12]))
print(binary_search(10, [1,2,3,4,5,6,7,8,9,10,11,12]))