SumSquared = 0
SquareSum = 0
for i in xrange(1, 101):
	SumSquared += i ** 2
for i in xrange(1, 101):
	SquareSum += i
SquareSum = SquareSum ** 2
print SquareSum-SumSquared