def finder(x,y):
    
    x = sorted(x)
    y = sorted(y)
    
    y.append(0)
    
    for i in range(len(x)):
        if x[i] == y[i]:
            pass
        elif x[i] != y[i]:
            return x[i]
        else:
            return x[-1]
        
        
    
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[8,7,6,5,4,3,2,1]),9)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)        

"""       
a = [9,8,7,6,5,4,3,2,1]
b = [8,7,6,5,4,3,2,1]

print(finder(a,b))"""   