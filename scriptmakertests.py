import unittest
import scriptmaker
import os

class testFunctions(unittest.TestCase):
    
    def setUp(self):
        os.remove('genscript.pl')

    def test1(self):
        '''check that no file exists after setUp'''
        self.assertFalse(os.path.exists('genscript.pl'))
    
if __name__ == '__main__':
    unittest.main()
