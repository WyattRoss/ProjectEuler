from bisect import bisect_left
from math import sqrt
from decimal import *
# sqrt(1000000000) = 31622
def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

# def is_prime(n):
# 	if n == 2:
# 		return True
# 	if n == 3:
# 		return True
# 	if n == 4:
# 		return False
# 	if n == 5:
# 		return True
# 	if n == 1:
# 		return 'Special Case'
# 	if n == 0:
# 		return 'Neither'
# 	if n < 0:
# 		return 'Number is not an integer'
# 	c = []
# 	for i in sieve(n):
# 		c.append(i)
# 	__primes = c
# 	g = str(n)
# 	# if prime is already in the list, just pick it
# 	if n <= 31622:
# 		i = bisect_left(__primes, n)
# 		return i != len(__primes) and __primes[i] == n
# 	# Divide by each known prime
# 	limit = sqrt(Decimal(g))
# 	for p in __primes:
# 		if p > limit: return True
# 		if n % p == 0: return False
# 	# fall back on trial division if n > 1 billion
# 	for f in range(31627, limit, 6): # 31627 is the next prime
# 		if n % f == 0 or n % (f + 4) == 0:
# 			return False
# 	return True
# print sieve
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))