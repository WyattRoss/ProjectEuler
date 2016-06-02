from Prime_Gen import *
def Factor(n):
	pFactors = []
	primes = sieve(n)
	for i in primes:
		if n % i == 0:
			pFactors.append(i)
	return pFactors