"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

number = 600851475143

# sieve up to n, if i want primes dividing n, enter sqrt(n)
def sieve_of_eratosthenes(n):
	
	# set up sieve
	sieve = range(n + 1)
	sieve[0] = None
	sieve[1] = None

	for i in range(1, n + 1):
		if sieve[i] != None:
			# is prime, delete all multiples after this
			for j in range(i + i, n + 1, i): # rewrite this to not recheck
				# if is multiple of i then delete
				# if j % i == 0 and j != i:
				sieve[j] = None
		#else:
			# is not prime and has already been deleted
		#	continue

	# clean array : may be a function to do this for me
	
	# this uses double the memory :/
	sieve_clean = []
	for i in range(n + 1):
		if sieve[i] != None:
			sieve_clean.append(i)
	# post question: is there a way to speed this up even more?
	return sieve_clean
	
# problem specific code
#number = 13195
factors = []

max_div = int(math.floor(math.sqrt(number)))

sieve = sieve_of_eratosthenes(max_div)

for i in sieve :
	if number % i == 0:
		factors.append(i);

print factors[-1]

# fine it works, but too slow :/
