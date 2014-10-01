[![Build Status](https://travis-ci.org/grimley517/A-Fun-Problem.svg)](https://travis-ci.org/grimley517/A-Fun-Problem)


#A fun Problem

## Instructions
- Clone this repo (don't fork it!)
- Figure out what to do and do it, adding more if you like
- tarball it and send along with your job application

##Development scheme

1. Raise an issue with the step

2. Branch the step Work on the issue in the new branch 
Name the branch with your username and the issue number note the existing naming scheme for branches

3. When the issue fixed bring it back into the master

##Documentation
### old Folder - The old folder contains;

- The legacy perl code (SillyFunction.pm)Some comment notes added
- a sample script to enter a string into the code (depreciated and not functioning - this was checking for scalar input to the Silyfunction.pm module
- A dynamic script maker (script maker.py) (depreciated and not functioning - used to experiment with different methods of putting a list of Hashes into the original module
- A runner (runner.py to run the perl script from a pythonic place
- tests for the runner and scriptmaker(runnerTest.py and scriptmakerTests.py)

### New folder - The new folder contains;

- The refactored code (refactored.py)
- unit tests for the refactored code (refactoredTest.py)

The refactored code has been written in object syntax with an eye on simplicity and flexibility.  Since memory is cheaper than process time I refactored this with the plan that this might be used in a more incremental fashion.  Products can now be added to the group class either individually, or in a list sequence.  The Time to add items to the group is in the order of O(n) for a list and O(1) for an individual item.  Retrieval can be either performed at O(n) as a list, or O(1) as a generator.

####Class “refactored”

construction by entering either an item as a dictionary with keys ‘brand’ and ‘type’

Simple Example 1 - setting up using a list of dicts, and returning a list of dicts
```python
import refactored
group = refactored.groupedProducts([{‘brand’:’foo’, ‘type’:’bar’},{‘brand’:foo’, ‘type’:’bar’}])

print (group.getGrpList())
```
This will return a list of unique {brand : type} pairs

Simple Example 2 - setting up using a product dicts, and generating items from the 
```python
import refactored
group = refactored.groupedProducts({‘brand’:’foo’, ‘type’:’bar’}),
group.add{‘brand’:foo’, ‘type’:’bar’}])

print (group.genGrpItem())
```



