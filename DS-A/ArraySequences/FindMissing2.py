def finder(arr1,arr2):
    
    # Sort the arrays
    arr1.sort()
    arr2.sort()
    
    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2): # Zip is a fenaaa thing!!
        if num1!= num2:
            return num1
    
    # Otherwise return last element
    return arr1[-1]