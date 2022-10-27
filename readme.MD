## Problem 

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

## Condtions 
o You cannot import a library that solves it instantly
o The methods add(), less(), greater(), and between() should have
constant time O(1)
o The method build_stats() can be at most linear O(n)

## Approach

Use a defaultdict to store values and take advantage of counting. Use 

#### How to run

Please use Makefile comamnds on Linux system:
 - make simulate
 - make test