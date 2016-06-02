import Prime_Gen
tot = 0
for i in Prime_Gen.sieve(2000000):
	tot += i
print tot 