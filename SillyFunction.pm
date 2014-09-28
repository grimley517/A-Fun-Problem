#
# Instructions
#
# 1. Figure out what this function does
# 2. Write a unit test for it
# 3. Refactor for readability and efficiency
#
# NOTE: Do regular commits that show agile style iterations through the problem.
# If you prefer a different language, you can provide your solution in PHP, 
# Python or Javascript too.
#
package SillyFunction;
# package is simmilar to the class keyword in python

sub group_products {
    #sub is simmilar to the def keyword in python
    #this is a constructor for the class.
  my $products = shift;
  # the $ sign signifies that products is scalar (string, number, reference or file handle
  # shift is used to assign the functions arguments to $products
  # the my keyword defines the scop as beloning private to the package
  my %brand_type = ();
  # the % sign signifies a hash (dictionary)  essentially an empty dict
  my $grouped_products = [];
    # again a scalar variable, This is a reference to an empty array, like an empty list in python
  

  foreach (@{$products})
  # the @ sign denotes a list (one dimensional array) this is a loop which converts the string held in $products into
    # this would be set by for for product in products: $_ indicates the product variable
  # a list seperated by spaces the product in products gets put into the special $_ variable
    
    {
      $brand_type{$_->{brand}} ||= {};
        #set $brand_type to  some variable called brand ||= makes the default brand a hash reference
      $brand_type{$_->{brand}}->{$_->{type}} = 1;
    }
  foreach (sort keys %brand_type)
    {
      my $brand = $_;
      foreach (sort keys %{$brand_type{$brand}}) 
      {
        push(@{$grouped_products},{ brand => $brand, type => $_});
      }
    }
  $grouped_products;
  }

1;
