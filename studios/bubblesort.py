#studio from class may8 - BubbleSort
########################

def swap(a, b):
	'''helper function that swaps two integers'''
    return [b, a]

def bubble_sort(list):
	'''sort the input list by swapping elements that are out of order'''
    # set while loop condition
    is_sorted = False
    # continue looping until sorting is complete
    while is_sorted == False:
        
        nswaps = 0
        # loop over the list and compare each index with the next
        for num in range(len(list)-1):
            a = list[num]
            b = list[num+1]

            # if a larger number is in front, use swap function and replace those two list indices
            # increase swaps count - while this number > 0, more sorting must be done
            if a > b:
                nswaps += 1
                list[num:num+2] = swap(a,b)
        
        # when the for loop no longer results in any swaps, list is sorted!        
        if nswaps == 0:
            is_sorted = True
                
    return list
        
                

