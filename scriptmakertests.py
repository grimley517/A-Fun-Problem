import unittest
import scriptmaker
import os

class testFunctions(unittest.TestCase):
    
    def setUp(self):
        if os.path.exists('genscript.pl'):
           os.remove('genscript.pl')

    def test1(self):
        '''check that no file exists after setUp'''
        self.assertFalse(os.path.exists('genscript.pl'))#test1 fails - genscript present after setup

    def test2(self):
        ''' Check for presence of file after generate function called'''
        scrip = scriptmaker.script()
        scrip.generate()
        self.assertTrue(os.path.exists('genscript.pl'))#test 2 fails - scriptmake does not make script

    def test3(self):
        '''check for replacement of argument and setup variables, string)'''
        scrip = scriptmaker.script(argument = 'foo')
        scrip.generate()
        self.assertTrue(os.path.exists('genscript.pl'))
        with open('genscript.pl')as file:
            text = file.read()
            self.assertIn('my $args = foo;', text)#test3 fails - foo not passed into argument of script, or line wrong

    def test4(self):
        '''check for replacement of argument and setup variables, list'''
        scrip = scriptmaker.script(argument = ['foo', 'bar'])
        scrip.generate()
        self.assertTrue(os.path.exists('genscript.pl'))
        self.assertEqual(scrip.setup,'my @argument = qw ( foo bar );')#test 4 fails - argument not passed correctly
        self.assertEqual(scrip.argument, '\@argument')#test4 fails - list reference wrong
                         
        with open('genscript.pl')as file:
            text = file.read()
            self.assertIn('my $args = \@argument;', text)#test4 fails - not passed into argument of script, or line wrong


    
    def test5(self):
        '''check for replacement of argument and setup variables, dict'''
        scrip = scriptmaker.script(argument = {'foo': 'bar', 'one':1})
        scrip.generate()
        self.assertTrue(os.path.exists('genscript.pl'))
        self.assertEqual(scrip.setup,'my %argument = qw ( foo bar one 1 );')#test 5 fails - argument not passed correctly
        self.assertEqual(scrip.argument, '\%argument')#test5 fails - dict reference wrong
                         
        with open('genscript.pl')as file:
            text = file.read()
            self.assertIn('my $args = \%argument;', text)#test5 fails - not passed into argument of script, or line wrong


        
    
if __name__ == '__main__':
    unittest.main()
