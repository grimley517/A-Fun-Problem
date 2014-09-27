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

sub group_products {
  my $products = shift;
  # the $ sign signifies that products is scalar (string, number, reference or file handle
  # shift is used to assign the functions arguments to $products
  my %brand_type = ();
  # the % sign signifies a hash (dictionary)  essentially an empty dict
  my $grouped_products = [];
    # again a scalar variable,
  

  foreach (@{$products})
  # the @ sign denotes a list (one dimensional array) this is a loop which converts the string held in $products into
  # a list and then
    {
      $brand_type{$_->{brand}} ||= {};
      $brand_type{$_->{brand}}->{$_->{type}} = 1;
    }
  foreach (sort keys %brand_type)
    {
      my $brand = $_;
      foreach (sort keys %{$brand_type{$brand}}) 
      {
        push(@{$grouped_products}, 
          { 
            brand => $brand, type => $_
          });
      }
    }
  $grouped_products;
  }

1;
