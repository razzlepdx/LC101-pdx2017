def binary_search(my_list, my_item):
    # ints used to represent an index in my_list
    low = 0
    high = len(my_list) - 1
    
    # base conditional 1 - high and low cannot swap places
    while low <= high:
        # int representing the index of the midpoint in the list
        mid = (low + high)//2
        # the actual item in the list, located at the midpoint index
        guess = my_list[mid]
        
        # base conditional 2 - midpoint guess is equal to the item we want!
        if guess == my_item:
            return "Found " + str(my_item) + " at index: " + str(mid) + "."
        
        # recursive conditional - guess was too high
        # reduces the high index to 1 less than the midpoint
        if guess > my_item:
            high = mid - 1
        # recursive conditional - guess was too low
        # increases the low index to the midpoint index + 1    
        else:
            low = mid + 1
    
    return "Couldn't find " + str(my_item) + " in this list."

my_list = [1,3,5,7,9]

print(binary_search(my_list, 4)) 
print(binary_search(my_list, 7)) 
print(binary_search(my_list, -1))
print(binary_search(my_list, 1))