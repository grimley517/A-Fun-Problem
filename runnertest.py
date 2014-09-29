import runner as run
import unittest

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
        

if __name__ == '__main__':
    unittest.main()
