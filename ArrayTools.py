def listCounts(lst):
	Counts = {}
	for i in list(set(lst)):
		Counts[i] = None
	for key in Counts:
		count = 0
		for i in lst:
			if i == key:
				count += 1
		Counts[key] = count
	return Counts
def listMode(lst):
	counts = listCounts(lst)
	Largest = 0
	Lkey = None
	for key in counts:
		if counts[key] > Largest:
			Lkey = key
			Largest = counts[key]
	return Lkey
def listAverage(lst):
	sm = sum(lst)
	return sm/len(lst)
def listSum(lst):
	tot = 0
	for i in lst:
		tot += i
	return tot
def listProd(lst):
	st = 1
	for i in lst:
		st *= i
	return st
def subarrays(array, length):
	c = len(array)-1
	c -= length
	All = []
	for i in xrange(c):
		subarray = []
		for b in xrange(length):
			subarray.append(array[i+b])
		All.append(subarray)
	return All