import subprocess

class perlRunner():
    def __init__ (self,  args = [], script = "script.pl"):
        self.script = script.lower() #to be commercial this would need some input checking.
        self.args = args
        self.cmd = ["perl {0}".format(self.script), ' '.join(self.args)]

    def call(self):
        ''' Gets the output from the script to be run
        '''
        return (subprocess.check_output(self.cmd, shell = True))

    def code(self):
        '''Gets the return code from the script to be run
        '''
        return (subprocess.call(self.cmd, shell = True))
        
