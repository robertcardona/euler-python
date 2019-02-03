"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

import math

# send the seive in so we don't have to recalculate

def sieve_of_erotosthenes(n):
	sieve = range(n + 1)
	sieve[0] = None
	sieve[1] = None

	for i in range(1, n + 1):
		if sieve[i] != None:
			for j in range(i + i, n + 1, i):
				sieve[j] = None

	sieve_clean = []
	for i in range(n + 1):
		if sieve[i] != None:
			sieve_clean.append(i)
	
	return sieve_clean

# find all primes from 1 to n
def is_prime(n):
	prime = True
	
	return prime

def max_power_dividing(n):
	power = 1

	return 0

n = 22

primes = sieve_of_erotosthenes(n)

gcd = 1

for prime in primes:
	
	power = 1
	while math.pow(prime, power) < n:
		power = power + 1
	
	power = power - 1
	gcd = gcd * int(math.pow(prime, power))

print gcd
