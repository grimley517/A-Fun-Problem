import unittest
import refactored

class testFunctions(unittest.TestCase):
    def test1(self):
        '''Check that a sinlge item can be entered, and retrieved'''
        item = {'brand':'citroen', 'type':'car'}
        expected = [{'brand':'citroen', 'type':'car'}]
        testVal = refactored.groupedProducts(item).getGrpList()
        self.assertEqual(expected, testVal) #test 1 fails output not as expected

    def test2(self):
        '''check that two different items can be entered, and retrieved'''
        items = [{'brand':'citroen', 'type':'car'},
                 {'brand':'honda', 'type':'bike'}]
                 
        expected1 = {'brand':'citroen', 'type':'car'}
        expected2 = {'brand':'honda', 'type':'bike'}
        testVal = refactored.groupedProducts(items).getGrpList()
        self.assertIn(expected1, testVal) #test 2 fails - Item 1 not in answer
        self.assertIn(expected2, testVal) #test 2 fails - Item 2 not in answer

    def test3(self):
        '''check that two Simmilar items can be entered, and retrieved without duplication'''
        items = [{'brand':'citroen', 'type':'car'},
                 {'brand':'citroen', 'type':'car'}]
                 
        expected = {'brand':'citroen', 'type':'car'}
        testVal = refactored.groupedProducts(items).getGrpList()
        self.assertIn(expected, testVal) #test 3 fails - Item not in answer
        self.assertEqual(len(testVal), 1) #test 3 fails - Answer too long - shows duplication

    def test4(self):
        '''check that output list is sorted by Type

        This is also checking generator output'''
        items = [{'brand':'citroen', 'type':'car'},
                 {'brand':'honda', 'type':'bike'}]
        expected1 = {'brand':'honda', 'type':'bike'}            
        expected2 = {'brand':'citroen', 'type':'car'}
        
        testgrp = refactored.groupedProducts(items)
        self.assertIn(expected1, testgrp.genGrpItem()) #test 4 fails - Item 1 not in order
        self.assertIn(expected2, testgrp.genGrpItem()) #test 4 fails - Item 2 not in order
        
if __name__ == '__main__':
    unittest.main()

