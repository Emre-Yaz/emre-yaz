def pair_sum(rsrc,trgt):
    
    rlist = []
    
    for i in rsrc:
        for j in rsrc: 
            
            # Sum all the elements of rsrc with each other
            if i+j == trgt: 
                # To prevent half of the target from colliding with itself
                if i==j and rsrc.count(i) < 2:
                    pass
                # To prevent duplicates
                elif (i,j) in rlist:
                    pass
                # Add it to the list as it meets the conditions
                else:
                    rlist.append((i,j))
                    # Eliminate these elements to prevent duplicates (even if their places are changed)
                    rsrc.remove(i)
                    rsrc.remove(j)
                    
            print(rlist) #To see how it works
    
    return print(len(rlist)) #Print to learn how many combinations of pairs we have
    

##########################################################################################
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)"""

pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) # (3,7) or (7,3) won't be counted as one of the pairs