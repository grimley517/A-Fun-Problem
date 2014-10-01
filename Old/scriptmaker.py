import os

class script:

    def __init__(self, argument = '$_'):
        if isinstance(argument, dict):
            self.setup = self.hashSetup(argument)
            self.argument = self.hashArgs(argument)
        elif isinstance(argument, list):
            self.setup = self.listSetup(argument)
            self.argument = self.listArgs(argument)
        else:
            self.argument = argument
            self.setup = '/n'

    def __del__(self):
        os.remove('genscript.pl')

    def generate(self):
        with open('genscript.pl', 'wt') as file:
            file.write("""use SillyFunction;
print 'started \\n';
{setup}
my $args = {arguments};
my $result = SillyFunction -> group_products ($args);\n
foreach (@{{$result}})\n
{{ \nprint 'brand is $_{{brand}}\\n';\nprint 'type is $_{{type}}\\n';\n}}\n;\n
            """.format (arguments=self.argument, setup = self.setup))#really odd indentation = although I hope it dosen't affect result.
            

    def hashArgs(self,argument):
        argument = '\%argument'
        return (argument)
    
    def hashSetup(self,argument):
        answer = ""
        for key, value in argument.items():
            key = str(key)
            value = str(value)
            answer = answer + " {0} {1}".format(key, value)
        answer = "my %argument = qw ({0} );".format(answer)
        return (answer)
    
    def listArgs(self,argument):
        argument = '\@argument'
        return (argument)
        
    
    def listSetup(self,argument):
        #if the fist thing in the list is a dict, then assume its a list of dicts
        if isinstance(argument[0],dict):
            answer = ""
            i=0
            for dictItem in argument:
                answer = answer + 'my $dict{0}_ref = {{ '.format(i)
                for key, value in dictItem.items():
                    answer = answer + '{1}=>{2} ,'.format(i, key, value)
                i +=1
                answer = answer [:-2] #removes last comma
                answer += '};\n'
            answer = answer + ' my @argument = ['
            j=0
            while j<i:
                answer = answer + '$dict{0}_ref , '.format(j)
                j+=1
            answer = answer[:-2]#again gets rid of last comma
            return (answer + ' ];')
        else:
            argument = map(str, argument)
            argument = " ".join(argument)
            argument = "my @argument = qw ( {0} );".format(argument)
            return (argument)
    
