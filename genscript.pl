use SillyFunction;
            print 'started //n';
            my %argument = qw ( foo bar one 1 );
            my $args = \%argument;
            my $result = SillyFunction -> group_products ($args);
            my @results = @{$result};
            foreach (@results){
            print 'a result is $_';
            }
            1;
            