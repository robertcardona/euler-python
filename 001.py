"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import math

# todo: given a set {x_1,...,x_n} of numbers, write an algorthim that 
# returns all possible products of elements in the set, e.g.,
# {2, 3, 5} would return {2, 3, 5, 6, 10, 15, 30}

debug = False

number = 1000

sum = 0

largest_in_number = int(math.floor(number/3));
for i in range(0, largest_in_number):
	if ((i + 1) * 3 < number):
		sum += (i + 1) * 3
		if debug: print (i + 1)*3

largest_in_number = int(math.floor(number/5));
for i in range(0, largest_in_number):
	if ((i + 1) * 5 < number):
		sum += (i + 1) * 5
		if debug: print (i + 1)*5

largest_in_number = int(math.floor(number/15));
for i in range(0, largest_in_number):
	if ((i + 1) * 15 < number):
		sum -= (i + 1) * 15
		if debug: print (i + 1)*15
print sum
