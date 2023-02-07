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
    
    extractor(arr)
    
    print(arr)
    
    
LCS([-2,-3,4,-18,20,-2,1,10,5,-3])  #34
   
