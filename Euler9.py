from ArrayTools import *
import itertools
import math, sys
def isPythag(a, b, c):
	a2 = a**2
	b2 = b**2
	c2 = c**2
	if a2 + b2 == c2:
		return True
	return False
candidates = []
for a in range(1000):
	for b in range(1000):
		c = a**2 + b**2
		c = math.sqrt(c)
		if isPythag(a, b, c) == True and a + b + c == 1000:
			print a*b*c
			sys.exit