import itertools
def nDigPandigs(digits, z):
	toFind = ''
	pandigs = []
	if z == 0:
		for i in range(0, digits):
			toFind += str(i)
	else:
		for i in range(1, digits+1):
			toFind += str(i)
	for i in itertools.permutations(toFind):
		pandigs.append(int(''.join(i)))
	return pandigs
def isPandigital(i):
	c = str(i)
	try:
		c.index('0')
		z = 0
		print 'h'
	except ValueError:
		z = 1
		print 'h'
	l = nDigPandigs(len(c), z)
	try:
		l.index(i)
		return True
	except ValueError:
		return False