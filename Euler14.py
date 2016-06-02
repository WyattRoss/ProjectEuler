import operator
def Collatz(i): #recursive because why not
	global cycleLen
	if i == 1:
		return cycleLen
	elif i % 2 == 0:
		n = i/2
	else:
		n = i*3
		n += 1
	cycleLen += 1
	print cycleLen
	Collatz(n)
nums = {}
for i in xrange(1, 1000000):
	loopthroughs = 1
	cycleLen = 1
	nums[i] = Collatz(i)
	print i
sorted_x = sorted(nums.items(), key=operator.itemgetter(1))
print sorted_x[-1]