def waysTosum(lst, sum):
	target = sum
	items = lst
	ways = [1] + [0]*target
	for item in items:
	    for i in range(item, target+1):
			ways[i] += ways[i-item]
	return ways[target]