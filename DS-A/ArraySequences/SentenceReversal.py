def rev_word(s):
    
    s = s.strip()
    s = list(s)
    
    delcount = 0
    delindex = []
    reslist= []
    res=""
    ict=0
    piece = ""
    
    for i in range(len(s)):
        if s[i] == " " and s[i+1] == " ":
            delindex.append(i-delcount)
            delcount +=1
    
    for i in delindex:
        del s [i]
        
    for i in s:
        if i != " ":
            piece += i
        else:
            reslist.append(piece)
            piece = ""
    reslist.append(piece)
    
    reslist.reverse()
    
    for i in reslist:
        res += i
        if i != reslist[-1]:
            res += " "
            
    return res

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)