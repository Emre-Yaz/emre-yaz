def anagramcheck(txt1, txt2):
    
    #To ignore uppercases
    txt1 = txt1.lower() 
    txt2 = txt2.lower() 
    
    #To ignore whitespaces
    txt1 = txt1.replace(" ","") 
    txt2 = txt2.replace(" ","") 
    
    if len(txt1) != len(txt2):
        return False #print("They are not even same lenght")
        
    for i in txt1:
        if i in txt2:
            return True #print(txt2 + " is an anagram of " + txt1 + ".")
        else:
            return False #print(txt2 + " is not an anagram of " + txt1 + ".")
    
####################################################################################################
################################--------TESTING--------#############################################
####################################################################################################
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagramcheck)