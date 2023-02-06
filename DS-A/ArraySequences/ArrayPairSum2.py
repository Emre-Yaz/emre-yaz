def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
        print(sorted(output))
    
    
    # FOR TESTING
    return len(output) 
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],13))