def divisors (i, includeI1or0):
	divs = []
	for z in range(1, i/2+1):
		if i % z == 0:
			divs.append(i)
	if includeI1or0 == 1:
		divs.append(i)
	else:
		pass
	return divs