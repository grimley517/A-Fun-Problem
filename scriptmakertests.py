import unittest
import scriptmaker
import os

class testFunctions(unittest.TestCase):
    def setUp(self):
        os.remove('genscript.pl')
        print ('.\n')

    def test1(self):
        '''check that no file exists after setUp'''
        pass
    
if __name__ == '__main_':
    unittest.main()