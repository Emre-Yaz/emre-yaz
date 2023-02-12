# Eliminates the negative elements on both the front and back end.
def extractor(a): 
    
    delindex = []
    
    for i in range(len(a)):
        if a[i] < 0:
            delindex.append(0)
        else:
            break
    
    for i in range(1,len(a)+1):
        if a[-i] < 0:
            delindex.append(-1)
        else:
            break
    
    for i in delindex:
        del a [i]
    
    return a

def LCS(arr):
    
    if len(arr)==0:
        return 0
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
        
    return max_sum
    
    
print(LCS([-2,-3,4,-18,20,-2,1,10,5,-3]))  #34
   
