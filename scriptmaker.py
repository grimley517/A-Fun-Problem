with open('genscript.pl', 'wt') as file:
    file.write("""use SillyFunction;\nprint 'started /n';\nmy $args = {arguments};
    my $result = SillyFunction -> group_products ($args);
    my @results = @{{$result}};
    foreach (@results){{
    print 'a result is $_';
    }}
    1;
    """.format (arguments='$_'))