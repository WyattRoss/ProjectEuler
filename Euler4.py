import itertools, ArrayTools
combs = []
tot = 0
def isPal(i):
	c = str(i)
	if c == c[::-1]:
		return True
	return False
for i in itertools.permutations(range(100, 1000), 2):
	c = sorted(i)
	combs.append(tuple(c))
combs = set(combs)
lgst = 0
for i in combs:
	tmpProd = ArrayTools.listProd(i)
	if tmpProd > lgst and isPal(tmpProd) == True:
		lgst = tmpProd
print lgst