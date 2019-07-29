"""
TestSuite for parseBRENDA
"""
import unittest
import parseBRENDA

class ParseBRENDATest(unittest.TestCase):
    
    def setUp(self):
        # Setup test environment
        pass
    
    def tearDown(self):
        # Cleanup test environment
        pass
    
    def test_01_Whatisit(self):
        """ 1: Test BRENDA parse function """
        res = ''
        self.failUnless(res == "Hallo", "wrong result")

    def test_02_Hallo(self):
        """ 2: Test it again """
        self.failUnless(1 == 1, "test is right")
        
if __name__ == "__main__":
    unittest.main()
    