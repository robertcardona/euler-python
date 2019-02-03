"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def max_in_list(number_list):
	maximum = 0
	for number_obj in number_list:
		number = int(number_obj)
		if number > maximum:
			maximum = number
	return maximum

# is there a more efficient way to do this?
def is_palindrome(n):
	stringify = str(n)
	stringify_length = len(stringify)
	# cases ?	
	if (stringify_length % 2 == 0):
		# is even
		for i in range(0, stringify_length / 2):
			# compare i and len - i
			# print stringify[i] + stringify[stringify_length - i - 1]
			if (stringify[i] != stringify[stringify_length - i - 1]):
				return False
	else:
		for i in range(0, (stringify_length - 1)/2):
			if (stringify[i] != stringify[stringify_length - i - 1]):
				return False
		# is odd

	return True

palindromes = []
n = 1000 # for 1000 expect 906609
for i in range(1, n):
	for j in range(i, n):
		if is_palindrome(i * j):
			palindromes.append(i * j)
print max_in_list(palindromes) # remove duplicates

test = "this is a test string"
