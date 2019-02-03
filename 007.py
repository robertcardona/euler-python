"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

# how can I choose the sieve size such that it must contain the n^th prime?

import math

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

n = 10001
m = int(2 * math.ceil(n * math.log(n)))

print sieve_of_erotosthenes(m)[n - 1]

