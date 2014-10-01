import runner as run
import unittest
import scriptmaker

class testSequence(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        #checks that the perlrunner class is running a system command
        proc = run.perlRunner(args = ['-v'], script = ' ')
        self.assertEqual(proc.code(), 0)#test1 fails - basic process failed to run

    def test2(self):
        # Checks that the perl script can be run with exit code 0
        proc = run.perlRunner()
        self.assertEqual(proc.code(), 0)#test2 fails - script.pl may be wrong

    def test3(self):
        ''' This is not really a test method, just a way of automating a mini-fuzzer.

            this is to inject a number of arguments into the script and see what the outputs are
            '''
        testArgs = ['1 2 3 4 5 6 7 8 9 10']
        proc = run.perlRunner(args = testArgs)
        print(proc.call())
        """The output to this shows that the expected input is either a hash, or a list.  From the code I expect a hash,
        but I would like to see what it does with both at any rate.
        """

    @unittest.skip('scriptgenerator changed, this test is obsolete')
    def test4(self):
        print('trying to input a list via the script generator')
        testArgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        scrip = scriptmaker.script(argument = testArgs)
        scrip.generate()
        proc = run.perlRunner(script = 'genscript.pl')
        print(proc.call())
        del scrip
        '''the output to this indicates that it is not expecting a list'''

    @unittest.skip('scriptgenerator changed, this test is obsolete')
    def test5(self):
        print('trying to input a dict via the script generator')
        testArgs = {'brand':'citroen', 'type' : 'ax'}
        scrip = scriptmaker.script(argument = testArgs)
        scrip.generate()
        proc = run.perlRunner(script = 'genscript.pl')
        print(proc.call())
        del scrip
        '''the output to this indicates that it is not expecting a dict'''

    def test6(self):
        print('trying to input a list of dicts via the script generator')
        testArgs = [{'brand':'citroen', 'type' : 'car'},
                    {'brand':'citroen', 'type':'car'},
                    {'brand':'cripps', 'type':'bread'},
                    {'brand':'peugeot', 'type':'car'}]
        scrip = scriptmaker.script(argument = testArgs)
        scrip.generate()
        proc = run.perlRunner(script = 'genscript.pl')
        print(proc.call())
        del scrip
        '''the output to this indicates that it is not expecting a list of dicts'''

if __name__ == '__main__':
    unittest.main()
