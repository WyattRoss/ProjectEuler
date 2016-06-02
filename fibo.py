def fib(limit):
	fibonacci = [1, 1]
	index = len(fibonacci)-1
	newTerm = fibonacci[-1]
	while newTerm < limit:
		newTerm = fibonacci[index] + fibonacci[index-1]
		index += 1
		if newTerm < limit:
			fibonacci.append(newTerm)
	return fibonacci