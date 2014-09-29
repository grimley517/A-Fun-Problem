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

    def generate(self):
        with open('genscript.pl', 'wt') as file:
            file.write("""use SillyFunction;
            print 'started //n';
            {setup}
            my $args = {arguments};
            my $result = SillyFunction -> group_products ($args);
            my @results = @{{$result}};
            foreach (@results){{
            print 'a result is $_';
            }}
            1;
            """.format (arguments=self.argument, setup = self.setup))

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
        argument = map(str, argument)
        argument = " ".join(argument)
        argument = "my @argument = qw ( {0} );".format(argument)
        return (argument)
    
