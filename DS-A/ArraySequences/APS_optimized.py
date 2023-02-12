def pair_sum2(rsrc,trgt):
    
    rlist = []
    rsrc_set = set(rsrc)
    
    for i in rsrc:
        x = trgt - i
        
        if x in rsrc_set:
            while (x,i) not in rlist and (i,x) not in rlist:
                rlist.append((i,x))
                break
    return len(rlist)

from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum2)