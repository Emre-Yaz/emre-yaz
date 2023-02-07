def pair_sum(rsrc,trgt):
    
    rlist = []
    
    for i in rsrc:
        for j in rsrc: 
            
            # Sum all the elements of rsrc with each other
            if i+j == trgt: 
                a = min(i,j)
                b = max(j,i)
                # To prevent half of the target from colliding with itself
                if a==b and rsrc.count(a) < 2:
                    pass
                # To prevent duplicates
                elif (a,b) in rlist:
                    pass
                # Add it to the list as it meets the conditions
                else:
                    rlist.append((a,b))

    return len(rlist) #Print to learn how many combinations of pairs we have
    

##########################################################################################

from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)

#print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)) # (3,7) or (7,3) won't be counted as one of the pairs