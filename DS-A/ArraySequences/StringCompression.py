def compress(inp):
    
    count = 1
    out = ""
    
    for i in range(len(inp)):
        if inp[i] not in out:
            out += inp[i]
        
        if i < len(inp) - 1 and inp[i] == inp[i+1]:
            count += 1
        else:
            out += str(count)
            count = 1
    
    return out

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)