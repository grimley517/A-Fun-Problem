use SillyFunction;
print 'started /n';
my $args = $_;
    my $result = SillyFunction -> group_products ($args);
    my @results = @{$result};
    foreach (@results){
    print 'a result is $_';
    }
    1;
    